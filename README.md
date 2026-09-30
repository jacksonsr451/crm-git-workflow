# Git Workflow CRM

Camada de gestão de trabalho sobre providers SCM. GitHub e GitLab permanecem fontes de verdade dos respectivos dados nativos; esta aplicação fornece contexto, workflow, visualizações, colaboração estruturada, sincronização e projeções locais.

## Estado do projeto

Esta fase contém somente documentação de produto, domínio e arquitetura. Não há código de produção, migrations, frontend ou integração implementados.

## Documentação

- [Visão](docs/product/vision.md)
- [Escopo e MVP](docs/product/scope.md)
- [Requisitos funcionais](docs/requirements/functional-requirements.md)
- [Regras de negócio](docs/requirements/business-rules.md)
- [Modelo de domínio](docs/domain/domain-model.md)
- [Ownership dos dados](docs/architecture/source-of-truth.md)
- [Integração GitHub](docs/architecture/github-integration.md)
- [Integrações SCM](docs/integrations/overview.md)
- [Capabilities por provider](docs/integrations/provider-capabilities.md)
- [Modelo normalizado](docs/integrations/normalized-domain-model.md)
- [Sincronização](docs/architecture/synchronization.md)
- [Arquitetura](docs/architecture/overview.md)
- [Revisão documental](docs/review/documentation-review.md)
- [CI/CD](docs/development/ci-cd.md)

## Premissas verificadas

As decisões dependentes de API estão registradas na [documentação de integrações](docs/integrations/overview.md), com links para documentação oficial consultada em 2026-09-30. Capabilities podem mudar por provider, plano, versão e permissão; contratos devem ser revalidados antes de cada implementação.

## Princípios

1. Não criar um segundo work item local autoritativo.
2. Confirmar no provider mutações de dados cuja autoridade é externa.
3. Tratar webhooks como atualização rápida, não como garantia de consistência.
4. Isolar todos os dados por `workspace_id`.
5. Falha de sincronização deve ser visível e recuperável.

## License

Este projeto é software proprietário. Todos os direitos estão reservados. O acesso ao código-fonte não representa concessão de licença. Uso, cópia, modificação ou distribuição requerem autorização prévia e expressa do titular. Os termos completos estão disponíveis no arquivo [LICENSE](LICENSE).

## Legal and Security Documents

- [Terms of Service (Draft — Pre-Launch)](TERMS.md)
- [Privacy Policy (Draft — Pre-Launch)](PRIVACY.md)
- [Security Policy](SECURITY.md)
- [Contributing](CONTRIBUTING.md)
- [Contributor License Agreement (Draft)](CLA.md)
- [Third-Party Notices](THIRD_PARTY_NOTICES.md)
