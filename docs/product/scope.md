# Escopo

## MVP

Inclui autenticação, instalação do GitHub App, workspace, seleção de repositórios, importação e projeção de Issues, detalhe e hierarquia de sub-issues, assignees, comentários, atualizações estruturadas, workflow baseado em Project single-select Status quando disponível, board, webhooks, reconciliação e timeline combinada.

## Fora do MVP

IA, chat proprietário, vídeo, calendário completo, Gantt, timesheet, CRM, wiki, editor de documentos, microserviços, event streaming complexo e Kubernetes.

Também ficam adiados: notificações avançadas, busca full-text dedicada, dependências criadas pela aplicação, múltiplos Projects por workflow e relatórios financeiros.

## Corte recomendado

Dependências devem ser somente leitura no primeiro incremento, salvo validação de permissões e UX. Structured updates entram como comentário confirmado no GitHub mais metadata local; não devem bloquear o MVP com um novo tipo de conteúdo remoto.

## Critério de saída do MVP

Um workspace consegue instalar o App, selecionar repositórios, visualizar Issues e sub-issues, alterar com segurança um status/assignee/comentário quando autorizado, refletir alterações externas e recuperar divergências por reconciliação.
