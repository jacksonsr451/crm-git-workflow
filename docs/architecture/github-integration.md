# Integração GitHub

Este documento descreve apenas o adapter GitHub. O contrato comum, o modelo normalizado e a comparação com GitLab estão em [docs/integrations](../integrations/overview.md).

## Evidências oficiais consultadas em 2026-09-30

- [Sub-issues REST](https://docs.github.com/en/rest/issues/sub-issues): listar, parent, adicionar, remover e repriorizar; a página de produto documenta até 100 filhos por parent e até oito níveis.
- [Issue dependencies REST](https://docs.github.com/en/rest/issues/issue-dependencies): `blocked_by`, `blocking`, adicionar/remover.
- [Webhook events](https://docs.github.com/en/webhooks/webhook-events-and-payloads): `issues`, `issue_comment`, `issue_dependencies`, `installation`, `installation_repositories`, delivery id, payload cap de 25 MB.
- [Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects): views table/board/roadmap, sincronização bidirecional e campos; até 50 fields por Project.
- [GitHub App permissions](https://docs.github.com/en/apps/creating-github-apps/registering-a-github-app/choosing-permissions-for-a-github-app): mínimo privilégio; sucesso depende de app e, para user token, usuário.
- [Webhook validation](https://docs.github.com/en/webhooks/using-webhooks/validating-webhook-deliveries): HMAC SHA-256, comparação constante e secret.
- [REST rate limits](https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api): installation token tem mínimo de 5.000/hora, limites secundários e headers autoritativos.

## Decisões

- GitHub App é mecanismo principal; PAT não é arquitetura de produção.
- REST é padrão para Issues, comments, sub-issues e dependencies. GraphQL só será usado quando reduzir round trips ou for necessário para Projects, após contract test.
- Solicitar inicialmente Issues read/write, Metadata read, Projects read/write conforme uso, e permissões de organização apenas se seleção/membership exigir.
- Issue webhooks necessários: `issues`, `issue_comment`, `issue_dependencies`, `installation`, `installation_repositories`, além de `projects_v2`/eventos aplicáveis após confirmação do contrato atual.

## Limitações e cautelas

Sub-issues cruzam repositórios conforme a documentação de UI, mas o endpoint REST de add exige mesmo owner; validar combinação owner/repository no ambiente alvo. Reordenação é suportada por endpoint específico. Não assumir cursor ou cobertura total de timeline; reconciliação deve usar paginação e checkpoints próprios. Os limites podem variar por GitHub Enterprise Cloud/Server e versão da API.

Issue fechada pode continuar com filhos abertos. Dependency não é automaticamente stage BLOCKED. Projects pode refletir alterações bidirecionais, mas o binding e as permissões precisam ser comprovados por instalação.
