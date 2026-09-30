# Invariantes do domínio

As invariantes normativas estão consolidadas em [domain-model.md](domain-model.md) e [business-rules.md](../requirements/business-rules.md). Em resumo:

- todo recurso tenant-owned é escopado por `workspace_id`;
- Issue/Comment/assignee/relação nativa usam identidade GitHub estável;
- parent tem no máximo um vínculo e não pode formar ciclo;
- mutation GitHub não é confirmada antes da API;
- inbox, comentários e comandos são idempotentes;
- state da Issue, stage de workflow, dependency e texto de bloqueio são conceitos independentes;
- pai e filho não fecham/reabrem em cascata;
- projeções obsoletas são sinalizadas, não apresentadas como certeza silenciosa.
