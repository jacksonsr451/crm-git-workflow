# Matriz de testes

| Regra de negócio | Requisito funcional relacionado | Teste |
|---|---|---|
| `BR-WORKITEM-001` | `FR-ISSUE-001`, `FR-ISSUE-002` | `test_repository_identity_is_provider_scoped` |
| `BR-ISSUE-008` | `FR-ISSUE-004` | `test_external_identity_is_provider_scoped` |
| `BR-COMMENT-002` | `FR-COMMENT-001` | `test_comment_and_structured_update_are_distinct` |
| `BR-COMMENT-004` | `FR-COMMENT-002` | `test_comment_and_structured_update_are_distinct` |
| `BR-COMMENT-005` | `FR-COMMENT-002` | `test_comment_and_structured_update_are_distinct` |
| `BR-WORKFLOW-001` | `FR-WORKFLOW-001` | `test_work_item_keeps_native_state_separate_from_workflow_stage` |
| `BR-ISSUE-003` | `FR-ISSUE-003` | Backlog: hierarchy contract |
| `BR-ISSUE-004` | `FR-ISSUE-003` | Backlog: parent/child cascade |
| `BR-ISSUE-005` | `FR-ISSUE-003` | Backlog: cycle detection |
| `BR-ISSUE-006` | `FR-ISSUE-002` | Backlog: progress calculation |
| `BR-WORKFLOW-006` | `FR-WORKFLOW-002` | Backlog: dependency/blocker separation |
| `BR-SYNC-001` | `FR-SYNC-001` | Backlog: webhook idempotency |
| `BR-AUTH-001` | `FR-AUTHZ-001` | Backlog: provider permission mapping |

`FR-ISSUE-*` and `FR-GITHUB-*` são IDs legados existentes; não foram renomeados silenciosamente. A generalização para GitLab aguarda decisão documental.
