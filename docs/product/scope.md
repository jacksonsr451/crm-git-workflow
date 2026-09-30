# Escopo

## MVP

Inclui conexão GitHub App, conexão OAuth/application GitLab, workspace, seleção de repositories/projects, importação e projeção de work items, detalhe e hierarquia, assignees, comentários, atualizações estruturadas, workflow nativo quando disponível, board, webhooks, reconciliação e timeline combinada.

## Fora do MVP

IA, chat proprietário, vídeo, calendário completo, Gantt, timesheet, CRM, wiki, editor de documentos, microserviços, event streaming complexo e Kubernetes.

Também ficam adiados: notificações avançadas, busca full-text dedicada, dependências criadas pela aplicação, múltiplos bindings de planejamento por workflow, suporte operacional amplo a versões GitLab Self-Managed e relatórios financeiros.

## Corte recomendado

Dependências devem ser somente leitura no primeiro incremento, salvo validação de permissões e UX por provider. Structured updates entram como comentário confirmado no provider mais metadata local; não devem bloquear o MVP com um novo tipo de conteúdo remoto.

## Critério de saída do MVP

Um workspace consegue conectar um provider, selecionar repositories/projects, visualizar work items e hierarquia, alterar com segurança status/assignee/comentário quando autorizado, refletir alterações externas e recuperar divergências por reconciliação.
