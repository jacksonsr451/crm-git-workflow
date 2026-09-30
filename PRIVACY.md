# Privacy Policy

**STATUS: DRAFT — PRE-LAUNCH**

This is a planning draft for a future service. It is not a final privacy notice and does not establish that the service is currently operating or compliant with any law. Processing activities, controller/operator roles, legal bases, retention periods, providers, contacts, and operational procedures require legal and technical validation before launch.

## 1. Introduction

The planned service will provide a management layer over connected SCM providers, initially GitHub and GitLab. This draft describes possible categories of information and intended safeguards without asserting that every category will be collected or stored.

## 2. Scope

This draft applies to the future application, website, GitHub App, account flows, workspaces, support channels, and related services to the extent they are launched. Specific products, domains, and entities covered are `TBD`.

## 3. Information We Collect

Depending on the feature and authorization, the service may receive or generate account identifiers, workspace membership and role data, configuration, saved views, synchronization state, audit records, logs, security events, and support communications. The final data inventory is `TBD`.

The service distinguishes:

- **Consulted**: data read from GitHub, GitLab, or another provider during a request or synchronization;
- **Processed**: data used to authenticate, authorize, display, synchronize, secure, or operate a feature;
- **Stored**: data persisted in application databases, audit stores, logs, or backups;
- **Temporary/cache**: data retained temporarily to serve a request, queue work, or improve performance.

Consulting or processing data does not by itself mean that the data is permanently stored.

## 4. Information Received from Connected Providers

Subject to granted permissions and actual feature use, the service may receive provider user IDs, usernames, public names, avatars, groups/organizations, repositories/projects, work items, assignees, comments/notes, labels, planning data, events, identifiers, connection details, and access-control information. The final scopes and fields are `TBD`.

The service should request minimum permissions and collect only data necessary for the selected functionality. Each connected provider remains the source of truth for its native data as described in the project architecture.

## 5. Authentication Information

Authentication may involve OAuth, GitHub App or GitLab application authorization data, session identifiers, connection identifiers, short-lived tokens, and security logs. Secrets and private keys should not be exposed to users or stored unnecessarily. The exact authentication provider, token storage, and session design are `TBD`.

## 6. Information We Do Not Intend to Collect

The project does not intend to collect passwords from GitHub users, GitHub personal access tokens supplied manually, payment data, precise location, biometric data, or unrelated sensitive personal data as part of the planned MVP. This is an intention, not a guarantee about all future features or data a user may submit in content. Final exclusions are `TBD`.

## 7. Purpose of Processing

Possible purposes include authentication, workspace authorization, displaying and filtering work, synchronizing provider data, executing user-requested provider actions, preventing abuse, debugging, security monitoring, auditing, service improvement, and complying with legal obligations. Purposes must be limited and documented before launch.

## 8. Legal Basis

For users in Brazil, the applicable LGPD roles, legal bases, legitimate-interest assessment, consent requirements, international-transfer mechanism, and rights procedures are **TBD and require legal review**. No statement in this draft constitutes a claim of LGPD compliance or a final legal-basis determination.

## 9. Data Storage

The planned architecture uses PostgreSQL for application data and projections. Other storage, logging, queue, backup, hosting, and monitoring providers are `TBD`. The service should separate source data, projections, temporary payloads, audit records, and secrets, and should apply access control and minimization.

## 10. Data Retention

Retention periods for account data, projections, comments, webhook payloads, logs, audit events, backups, and deletion records are `TBD`. Retention must be defined by purpose, legal requirement, operational need, and deletion capability before launch.

## 11. Data Sharing

Data may be transmitted to GitHub when a user requests or authorizes a corresponding operation, and may be shared with infrastructure providers necessary to operate the service. No final sharing list, disclosure basis, or provider inventory has been approved. Those details are `TBD`.

## 12. Third-Party Processors

`TBD` — subprocessors, hosting, database, logging, monitoring, email, analytics, and support providers have not been selected or documented.

## 13. International Data Transfers

`TBD` — hosting locations, provider transfer mechanisms, safeguards, and applicable cross-border requirements have not been determined.

## 14. Security

The planned security controls include least-privilege GitHub App permissions, HMAC webhook validation, secret management, tenant isolation, authorization checks, secure Markdown handling, rate limiting, auditability, and incident response. See [docs/architecture/security.md](docs/architecture/security.md) and [SECURITY.md](SECURITY.md). These plans do not constitute a guarantee of absolute security or a certification.

## 15. Cookies and Similar Technologies

`TBD` — cookie categories, session cookies, analytics, consent controls, and browser storage have not been finalized.

## 16. User Rights

Subject to applicable law and final process, individuals may have rights such as access, correction, deletion, portability, information about processing, and objection. The identity-verification process, request channel, deadlines, exceptions, and responsible party are `TBD`. No absolute right is promised where law provides exceptions.

## 17. Account and Data Deletion

Deletion workflows, propagation to projections, caches, logs, backups, audit records, and GitHub resources are `TBD`. Uninstalling the GitHub App or deleting an application account may stop future access but does not automatically delete GitHub content.

## 18. GitHub App Uninstallation

Uninstallation or revocation should stop API actions, mark affected data as inaccessible, process relevant GitHub events, and begin the defined deletion or retention workflow. Exact timing, retained audit information, and recovery behavior are `TBD`.

## 19. Children's Privacy

Age requirements and child-specific processing policy are `TBD`, subject to applicable law. The service is not currently launched and makes no representation about suitability for children.

## 20. Changes to this Policy

The final notice will describe how changes are communicated and when they take effect. Versioning and notification mechanisms are `TBD`.

## 21. Contact

`TBD` — no privacy contact, data protection contact, or legal entity information has been defined.
