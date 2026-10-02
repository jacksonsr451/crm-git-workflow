# Work Items API

## GET /api/v1/work-items

Lista work items normalizados de um repository acessível no workspace atual.

Este endpoint implementa o contrato de leitura previsto em `FR-ISSUE-001` e consome o caso de uso `ListWorkItems`.

## Autenticação e escopo

O endpoint exige usuário autenticado e membership válida no workspace atual.

Toda consulta deve ser resolvida dentro do workspace do contexto.

O `repository_id` deve identificar um repository pertencente ao workspace atual e acessível pela conexão com o provider.

A autorização local não substitui as permissões efetivas da conexão com o provider.

Um recurso fora do escopo autorizado não deve ter informações sensíveis expostas pela resposta.

## Request

```http
GET /api/v1/work-items?repository_id=<repository_id>
```

### Query parameters

| Parâmetro | Obrigatório | Tipo | Descrição |
|---|---|---|---|
| `repository_id` | Sim | `string` | Identificador interno do repository no workspace atual. |
| `cursor` | Não | `string` | Cursor opaco para continuação da paginação. |
| `limit` | Não | `integer` | Quantidade máxima de itens solicitados na página. |

`limit` deve ser positivo e respeitar o limite máximo definido pela aplicação.

`cursor` é opaco para o cliente e não deve ser interpretado ou construído externamente.

Parâmetros inválidos devem produzir erro de validação.

## Response

Uma consulta válida retorna:

```http
200 OK
```

```json
{
  "items": [
    {
      "id": "string",
      "provider": "github",
      "external_id": "string",
      "title": "string",
      "state": "open",
      "assignees": [],
      "labels": []
    }
  ],
  "next_cursor": "string-or-null"
}
```

### `items`

`items` contém somente work items pertencentes ao repository solicitado.

Uma consulta válida sem resultados retorna:

```json
{
  "items": [],
  "next_cursor": null
}
```

Lista vazia representa ausência legítima de resultados. Erros de provider, autorização ou capability não podem ser convertidos silenciosamente em lista vazia.

### Identidade

`id` representa a identidade normalizada exposta pela aplicação.

`external_id` preserva a identidade do recurso no provider e não deve ser tratado isoladamente como identificador global.

A identidade externa continua provider-scoped conforme as invariantes do domínio.

### `provider`

`provider` identifica o provider de origem do work item.

Somente valores suportados pelo domínio podem ser retornados, atualmente:

- `github`
- `gitlab`

O contrato HTTP não deve introduzir lógica específica de GitHub ou GitLab no application layer.

### `state`

`state` representa o estado nativo normalizado do work item.

Ele não representa `workflow_stage`.

State nativo e estágio do workflow permanecem conceitos distintos.

### `assignees`

`assignees` contém as identidades externas normalizadas atribuídas ao work item.

A API não deve assumir que um assignee possui usuário local correspondente.

### `labels`

`labels` contém as labels normalizadas fornecidas pelo provider.

Labels não representam workflow por padrão.

### `next_cursor`

`next_cursor` contém um cursor opaco quando houver continuação disponível.

Quando não houver próxima página:

```json
{
  "next_cursor": null
}
```

O cliente não deve interpretar a estrutura interna do cursor.

## Capabilities

A operação depende da capability necessária para leitura/listagem de work items na conexão e repository correspondentes.

Os estados de capability são:

- `SUPPORTED`
- `PARTIAL`
- `UNSUPPORTED`

`UNSUPPORTED` deve produzir erro explícito de capability.

Uma capability ausente ou não suportada não pode ser convertida silenciosamente em lista vazia.

`PARTIAL` deve preservar a semântica informada pela conexão/provider e não pode ser automaticamente tratado como `SUPPORTED`.

A camada de aplicação não deve implementar comportamento por meio de condicionais como:

```python
if provider == "github":
    ...
elif provider == "gitlab":
    ...
```

Diferenças entre providers devem permanecer encapsuladas nos adapters e capabilities.

## Error response

Erros utilizam o envelope:

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

### Mapeamento de erros

| Condição | HTTP | `code` | `retryable` |
|---|---:|---|---|
| Requisição ou query inválida | `422` | `validation_error` | `false` |
| Autenticação ausente ou inválida | `401` | `authentication_error` | `false` |
| Acesso não autorizado | `403` | `authorization_error` | `false` |
| Repository ou recurso não encontrado no escopo permitido | `404` | `not_found` | `false` |
| Capability necessária não suportada | `422` | `capability_not_supported` | `false` |
| Conflito reportado pelo provider | `409` | `provider_conflict` | `false` |
| Rate limit do provider | `429` | `provider_rate_limited` | `true` |
| Provider temporariamente indisponível | `503` | `provider_unavailable` | `true` |

Os erros normalizados do domínio/application devem ser traduzidos pela camada HTTP; o endpoint não deve expor exceções específicas do SDK/API do provider.

Erros de autenticação, autorização, capability, rate limit ou indisponibilidade não devem retornar `200` com `items: []`.

Respostas de erro não devem expor tokens, secrets, credenciais ou payload bruto do provider.

## Source of truth

O provider permanece source of truth para campos provider-native.

O endpoint expõe uma representação normalizada desses dados para a aplicação.

A existência deste endpoint não transforma work items externos em entidades locais autoritativas.

## Sync status

`FR-ISSUE-001` prevê `sync status` nas projeções listadas.

O contrato concreto de `sync_status` não é definido neste ciclo porque persistência, sincronização, idempotência e reconciliação pertencem aos ciclos posteriores.

O endpoint do Cycle 10 não deve inventar um estado de sincronização sem que o contrato de `SyncState` esteja definido.

A inclusão futura de `sync_status` deve preservar compatibilidade do contrato versionado.

## Critérios de aceitação do Cycle 10

O contrato é considerado atendido quando:

1. `GET /api/v1/work-items` exige `repository_id`.
2. uma consulta válida retorna `200`.
3. nenhum work item retorna `items: []`.
4. múltiplos work items preservam a representação normalizada.
5. `state` permanece separado de workflow.
6. identidade externa permanece provider-scoped.
7. erros normalizados são convertidos para o contrato HTTP.
8. capability não suportada gera erro explícito.
9. erros não são convertidos em lista vazia.
10. a implementação não contém branching específico de GitHub/GitLab no caso de uso.
11. os testes são determinísticos e não dependem de rede.
12. o provider permanece source of truth.
