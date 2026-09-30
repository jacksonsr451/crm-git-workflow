# Requisitos funcionais

## FR-AUTH-001
Descrição: autenticar usuário e associar identidade GitHub quando necessário. Ator: usuário. Pré: conta válida. Esperado: sessão segura e tenant selecionado; exceção: identidade revogada exige reautorização. Aceitação: usuário não acessa workspace sem membership.

## FR-WORKSPACE-001
Descrição: criar workspace e convidar membros. Ator: Owner/Admin. Pré: sessão autenticada. Esperado: membership com role e isolamento. Exceção: convite expirado/revogado. Aceitação: consulta de outro workspace retorna 404/403 sem vazamento.

## FR-GITHUB-001
Descrição: instalar GitHub App e listar instalações/repositórios autorizados. Ator: Owner/Admin. Pré: autorização GitHub. Esperado: instalação e permissões registradas; exceção: instalação removida/repositório não selecionado. Aceitação: somente repositórios acessíveis podem ser selecionados.

## FR-ISSUE-001
Descrição: importar e listar Issues. Ator: membro autorizado. Pré: repository selecionado. Esperado: projeções paginadas com título, state, assignees, labels e sync status. Aceitação: importação repetida é idempotente.

## FR-ISSUE-002
Descrição: visualizar detalhe e hierarquia. Ator: membro/viewer. Pré: Issue projetada. Esperado: body, comentários, children, dependencies, progresso e origem GitHub. Aceitação: pai fechado com filhos abertos é sinalizado.

## FR-ISSUE-003
Descrição: criar/associar/remover/reordenar sub-issue. Ator: membro com permissão GitHub. Pré: parent/child válidos. Esperado: API GitHub confirmada, relação atualizada. Exceção: ciclo, limite/API/permissão. Aceitação: sem fechamento automático de descendentes.

## FR-ISSUE-004
Descrição: alterar assignees, state e labels. Ator: membro autorizado. Pré: GitHub permite. Esperado: API antes da confirmação. Aceitação: conflito não sobrescreve mudança externa silenciosamente.

## FR-COMMENT-001
Descrição: criar, editar e excluir comentário. Ator: membro autorizado. Pré: Issue acessível. Esperado: operação GitHub, projeção idempotente. Aceitação: retry com mesma intenção não duplica.

## FR-COMMENT-002
Descrição: registrar structured update. Ator: membro. Pré: comentário permitido. Esperado: comentário formatado no GitHub e metadata local associada ao ID retornado. Aceitação: edição externa mantém conteúdo e atualiza timeline; metadata perdida degrada.

## FR-WORKFLOW-001
Descrição: configurar workflow e mapear Project Status. Ator: Owner/Admin. Pré: Project acessível. Esperado: stages ordenados, inicial/finais e mapeamento. Exceção: field removido gera degraded/read-only. Aceitação: nenhuma label é criada automaticamente para status.

## FR-WORKFLOW-002
Descrição: mover card no board. Ator: membro autorizado. Pré: card tem Project field mapeado. Esperado: mutation do field GitHub, confirmação e atualização. Exceção: permissão/race gera conflito/reload.

## FR-VIEW-001
Descrição: salvar view com filtros, ordenação e layout. Ator: membro. Pré: workspace. Esperado: configuração local por workspace. Aceitação: view não altera Issue.

## FR-ACTIVITY-001
Descrição: visualizar timeline combinada. Ator: membro/viewer. Pré: Issue acessível. Esperado: eventos GitHub identificados como externos e audit events como aplicação. Aceitação: não afirmar completude quando timeline/API não cobrir evento.

## FR-SYNC-001
Descrição: receber webhook. Ator: GitHub. Pré: endpoint ativo. Esperado: validar, persistir inbox, responder 2xx rapidamente e processar de modo idempotente. Exceção: assinatura/payload inválido rejeitado.

## FR-SYNC-002
Descrição: reconciliar repository/Issue. Ator: sistema/admin. Pré: instalação válida. Esperado: buscar API, detectar divergência, corrigir projeção e registrar resultado. Aceitação: itens deletados/transferidos recebem tombstone ou novo vínculo explícito.

## FR-SYNC-003
Descrição: recuperar sincronização falha. Ator: Admin/sistema. Esperado: retry, backoff, rate-limit awareness, status visível e reprocessamento seguro.

## FR-AUTHZ-001
Descrição: autorizar por role e GitHub permission. Ator: sistema. Esperado: exigir ambos para mutation. Aceitação: Viewer não muta; Admin sem permissão GitHub recebe erro acionável.

## FR-CONFLICT-001
Descrição: tratar edição concorrente. Ator: usuário. Pré: projection version antiga. Esperado: re-fetch e conflito para body/title/relations/status se `updated_at` mudou; operações idempotentes simples podem retry. Aceitação: nunca overwrite silencioso.
