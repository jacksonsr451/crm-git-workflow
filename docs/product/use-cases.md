# Casos de uso

- **UC-001 Conectar GitHub**: Admin instala App, escolhe conta e conclui callback.
- **UC-002 Selecionar repository**: Admin escolhe repositórios permitidos e inicia importação.
- **UC-003 Importar Issues**: sistema pagina e cria/atualiza projections idempotentes.
- **UC-004 Visualizar tarefa**: usuário vê dados nativos, origem e sync status.
- **UC-005 Visualizar hierarquia**: usuário navega parent/children e progresso.
- **UC-006 Alterar responsável**: membro autorizado envia mutation GitHub.
- **UC-007 Comentar**: membro autorizado cria comentário confirmado.
- **UC-008 Registrar atualização**: membro escolhe tipo, escreve mensagem e cria comentário + metadata.
- **UC-009 Alterar workflow**: Admin mapeia stages; membro move card se autorizado.
- **UC-010 Criar subtarefa**: usuário cria/associa Issue e parent via API oficial.
- **UC-011 Fechar tarefa**: mutation fecha a Issue, sem cascata.
- **UC-012 Reabrir tarefa**: mutation reabre a Issue e recalcula projeções.
- **UC-013 Visualizar atividade**: timeline diferencia GitHub e aplicação.
- **UC-014 Recuperar sincronização**: Admin solicita reconcile e acompanha erro/lag.
- **UC-015 Tratar conflito**: usuário recebe versão atual, sua intenção e opção de reaplicar.
