# Git Workflow CRM

Camada de gestão de trabalho sobre GitHub Issues. O GitHub continua sendo a fonte de verdade dos dados nativos de uma Issue; esta aplicação fornece contexto, workflow, visualizações, colaboração estruturada, sincronização e projeções locais.

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
- [Sincronização](docs/architecture/synchronization.md)
- [Arquitetura](docs/architecture/overview.md)
- [Revisão documental](docs/review/documentation-review.md)

## Premissas verificadas

As decisões dependentes da API estão registradas em [github-integration.md](docs/architecture/github-integration.md), com links para documentação oficial consultada em 2026-09-30. Capacidades do GitHub podem mudar; contratos devem ser revalidados antes de cada implementação.

## Princípios

1. Não criar uma segunda Issue local autoritativa.
2. Confirmar no GitHub mutações de dados cuja autoridade é do GitHub.
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
