# Convenções de API

Endpoints devem ser versionados e sempre resolvidos dentro do workspace do contexto. Mutations que tocam providers externos retornam `confirmed`, `pending`, `failed` ou `conflict`, além de `correlation_id`, `source_updated_at` e link de origem quando aplicável.

Comandos de criação/retry aceitam `Idempotency-Key`; comandos de edição aceitam `expected_version` ou `expected_updated_at`.

Paginação, filtros e ordenação são limitados e validados. Quando utilizada paginação por cursor, o cursor é opaco para o cliente.

Erros expõem código estável, mensagem segura, `correlation_id` e indicação de `retryable`, sem tokens, secrets, credenciais ou payload bruto do provider.

A implementação deve manter este contrato alinhado com [api-conventions.md](../architecture/api-conventions.md).

## Autenticação e workspace

Endpoints protegidos exigem usuário autenticado.

Toda operação deve ser resolvida dentro do workspace atual e respeitar membership e isolamento entre workspaces.

A autorização local não substitui as permissões efetivas da conexão com o provider.

Recursos fora do escopo autorizado não devem ter informações sensíveis expostas.

## Paginação

Endpoints de coleção podem utilizar paginação por cursor.

Quando utilizado:

- `cursor` é opaco para o cliente;
- `limit` deve ser um inteiro positivo;
- a aplicação deve impor um limite máximo;
- valores inválidos devem produzir erro de validação;
- ausência de próxima página deve ser representada por `next_cursor: null`.

O formato e os parâmetros específicos de cada coleção pertencem ao contrato do respectivo endpoint.

## Erros

Endpoints HTTP utilizam o seguinte envelope de erro:

```json
{
  "error": {
    "code": "string",
    "message": "string",
    "retryable": false,
    "correlation_id": "string"
  }
}
```

A camada HTTP é responsável por traduzir erros normalizados da aplicação/domínio para códigos HTTP e códigos estáveis da API.

Erros específicos de SDKs ou APIs de providers não devem atravessar diretamente o contrato HTTP.

Erros não devem ser convertidos silenciosamente em respostas de sucesso.

## Capabilities

Operações dependentes de funcionalidades externas devem respeitar as capabilities declaradas pela conexão/provider.

Capabilities não suportadas devem produzir resultado explícito e não podem ser silenciosamente tratadas como ausência de dados.

Uma capability `PARTIAL` não deve ser automaticamente tratada como `SUPPORTED`.

O comportamento específico de cada operação pertence ao contrato do respectivo endpoint.

## Contratos específicos

Convenções deste documento são compartilhadas por todos os endpoints.

Schemas, parâmetros, regras de negócio e mapeamentos específicos devem ser definidos nos respectivos contratos de API.

O contrato de listagem de work items está definido em [work-items.md](work-items.md).
