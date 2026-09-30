# CI/CD

## Estado atual

O repositório possui documentação e um backend Python inicial. Não existem frontend Node/Next.js, `package.json`, `pnpm-lock.yaml`, Dockerfile, migrations ou scripts de build. Por isso, os gates ativos validam documentação, backend e secrets reais no histórico/checkout.

## Workflows ativos

### `CI`

- Trigger: pull requests destinadas a `main` e push em `main`.
- Check: `CI / docs`.
- Valida arquivos obrigatórios, trailing whitespace, links locais Markdown e fechamento de blocos Mermaid.
- Permissão: `contents: read`.

### `CI / backend`

- Trigger: os mesmos eventos de `CI`.
- Executa em Python 3.11 com Poetry 2.4.0.
- Valida `poetry.lock`, instala dependências sem atualizar o lockfile e executa Ruff, formatter, mypy e `poetry run testrunner` na suíte estável.
- Confirma que `pyproject.toml` e `poetry.lock` não foram modificados durante o job.
- Permissão: `contents: read`.

### `Security`

- Trigger: pull requests destinadas a `main`, push em `main` e execução semanal agendada.
- Check: `Security / secrets`.
- Executa Gitleaks com action fixada por commit SHA.
- Não imprime secrets nem usa secrets de aplicação; `GITHUB_TOKEN` é o token efêmero padrão do workflow.
- Permissões: `contents: read` e `pull-requests: read` no job.

### Dependabot

`.github/dependabot.yml` atualiza apenas actions usadas pelo próprio repositório. Ecosystems Python e Node serão adicionados quando manifests e lockfiles existirem.

## Checks recomendados para `main`

Quando a proteção de branch for configurada remotamente, tornar obrigatórios:

- `CI / docs`
- `CI / backend`
- `Security / secrets`

Exigir o nome exato e estável do check. Não há configuração remota de branch protection nesta tarefa.

## Ativação progressiva

### Backend: `ACTIVE`

O backend inicial já possui `pyproject.toml`, `poetry.lock`, pacote Python e testes executáveis via `jsr-testrunner`. O job usa Python 3.11, conforme a configuração atual. PostgreSQL só entra como service container quando um teste de integração realmente depender dele. Alembic só será verificado quando existir.

### Frontend: `PREPARED`

Ativar quando existirem `package.json`, `pnpm-lock.yaml` e código frontend. O job deverá respeitar `packageManager`, usar Corepack/pnpm, instalar com `--frozen-lockfile` e executar somente scripts presentes. Não há build ou typecheck ativo agora.

### Dependency review: `PREPARED`

Adicionar quando houver manifests/lockfiles sujeitos a revisão de dependências. O gate deve ser habilitado em pull requests e sua disponibilidade/licenciamento deve ser confirmada no repositório antes de torná-lo obrigatório.

### CodeQL: `PREPARED`

Adicionar quando houver código Python ou JavaScript/TypeScript. A matriz deve conter somente linguagens detectadas no repositório, com `security-events: write` restrito ao job de análise.

### Container/SBOM: `NOT YET APPLICABLE`

Não existe Dockerfile de produção nem artefato distribuível. Quando existir, separar build, scan, SBOM e publicação; publicar somente em eventos autorizados, com tags de versão e SHA, nunca somente `latest`.

### Release: `PREPARED`

O modelo futuro é tag/release -> CI validado -> build -> artifact -> SBOM/provenance -> GitHub Release. Não criar `v1.0.0` nem tags artificiais enquanto o produto estiver em `0.x` e sem artefato.

### Deployment: `BLOCKED BY MISSING INFRASTRUCTURE`

Não há cloud provider, registry, staging ou production definidos. Não existe deploy funcional. Quando houver target, preferir OIDC a credenciais cloud permanentes, separar environments e promover o mesmo artefato produzido, sem rebuild por ambiente.

## Segurança e supply chain

- Actions de terceiros usadas atualmente são fixadas por SHA e possuem comentário de versão humana.
- `contents: read` é o default; não há `write-all`, `pull_request_target`, `@main`, `@master`, `continue-on-error: true` ou `|| true`.
- Pull requests de forks não recebem secrets de aplicação nem permissões de escrita.
- O cache não é usado enquanto não houver dependências; quando adicionado, a chave deve incluir lockfile e nunca incluir `.env`, tokens ou credentials.
- Gitleaks é o secret scanning ativo. Dependency scanning, CodeQL, container scanning, SBOM e provenance aguardam artefatos/manifests reais.
- A action de checkout em PR trabalha sobre o merge ref fornecido pelo evento `pull_request`; nenhum código de fork é executado em contexto privilegiado.

## Falhas

- Falha de documentação bloqueia `CI / docs`.
- Falha de lint, formatter, typecheck ou teste bloqueia `CI / backend`.
- Secret detectado bloqueia `Security / secrets` e deve ser removido/revogado, não apenas ocultado.
- Falhas futuras de lint, typecheck, teste, dependência, CodeQL, build ou scan devem falhar o job correspondente sem `continue-on-error`.
- Release não deve iniciar sem os gates aplicáveis concluídos.
- Deployment futuro deve promover um artifact existente; falha de promoção não deve gerar rebuild implícito.

## Equivalentes locais

O check documental pode ser reproduzido executando o mesmo bloco Python do workflow em uma máquina com Python 3. O backend pode ser validado em `backend/` com `poetry check --lock`, `poetry run ruff check .`, `poetry run ruff format --check .`, `poetry run mypy src` e `poetry run testrunner`. O secret scan pode ser reproduzido com uma versão fixada do Gitleaks instalada localmente. Jobs futuros de frontend devem expor comandos pnpm equivalentes.

## Branches e merge

`main` é a única branch permanente observada nesta auditoria. Recomenda-se pull request obrigatório, approvals, checks obrigatórios, resolução de conversas, branch atualizada antes do merge, force push desabilitado e exclusão desabilitada. Squash merge é a estratégia recomendada para manter o histórico principal compacto. Nenhuma configuração remota foi alterada.

## GitLab

GitLab é provider integrado ao produto, não o CI deste repositório. Não foi criado `.gitlab-ci.yml`; ele só deve ser adicionado se o código for hospedado no GitLab ou houver decisão explícita de duplicar a execução.
