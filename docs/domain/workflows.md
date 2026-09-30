# Workflows

## Modelo

Um workflow tem stages configuráveis e transições livres por padrão. Stage inicial é usado na apresentação/importação somente quando o Project field define valor; não se atribui valor local silenciosamente. Stages finais são apresentação, enquanto `Issue state=closed` permanece o estado nativo.

## Project

Recomendação MVP: um Project binding por workflow e um campo single-select escolhido explicitamente. O produto lê opções e nomes, salva apenas o mapeamento estável por option id e não presume que `Status` tenha nomes específicos. Projects oferece table, board, roadmap, filtros e campos; o produto adiciona UX focada em Issue e tenant.

## Alterações externas

Mudança no Project/GitHub atualiza a projeção. Field removido, Project removido ou opção renomeada deixa o workflow `degraded`, preserva histórico e impede drag-and-drop até remapeamento.

## Remoção

Stage em uso precisa ser remapeado para outra opção ou o workflow fica bloqueado. Não mudar Issue state automaticamente por mover coluna.

## Board

Card é uma IssueProjection. Drag-and-drop é comando de atualização do Project field. Se não houver binding editável, o board é read-only e explica por quê.
