# Edge cases

| Caso | Comportamento |
|---|---|
| Issue deletada | tombstone, card removido das views ativas, histórico indica indisponível |
| Issue transferida | atualizar repository/link se evento/API permitir; caso contrário refetch por origem e marcar revisão |
| Repository renomeado | manter ID, atualizar nome/URL por webhook/reconcile |
| Repository transferido | preservar ID e mover escopo se instalação/workspace autorizar; senão inacessível |
| Repository arquivado | leitura permitida conforme GitHub; mutations desabilitadas |
| Repository privado | somente se instalação e workspace tiverem acesso |
| Installation removida | suspender comandos, marcar projections e notificar Admin |
| Usuário removido da organização | refletir assignee externo; mutations que exigem usuário falham com explicação |
| Assignee removido | atualizar lista GitHub; não manter assignee local fantasma |
| Comentário deletado/editado | webhook atualiza corpo/tombstone; structured metadata permanece somente se comentário existir |
| Sub-issue movida | atualizar parent; recalcular ambos os pais |
| Pai fechado com filho aberto | preservar ambos e exibir alerta; sem cascata |
| Filho reaberto | reabrir apenas filho e recalcular progresso |
| Webhook duplicado | 2xx/idempotente sem efeito repetido |
| Webhook fora de ordem | comparar versão/timestamp; refetch quando incerto |
| Webhook perdido | reconciliação corrige |
| API indisponível | command pending/failed, retry seguro, UI mostra atraso |
| Rate limit | backoff conforme headers, não martelar API |
| Permissões alteradas | 403 encerra mutation e marca capability/sync degraded |
| Workflow field removido | workflow degraded/read-only até remapeamento |
| Project removido | desvincular com audit; preservar views locais sem status mutável |
| App suspensa | parar jobs/mutations e exibir estado |
| Mudança simultânea | expected version/re-fetch; conflito explícito para overwrite sensível |
