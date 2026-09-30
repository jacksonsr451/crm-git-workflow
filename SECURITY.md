# Security Policy

This repository contains a proprietary project currently in development. Security reports are welcome, but the project does not yet have public releases or a committed response SLA.

## Supported Versions

The project is pre-release and does not currently have public releases or supported versions. Support policy and supported-version definitions are `TBD`.

## Reporting a Vulnerability

Report suspected vulnerabilities privately through the security contact: **TBD**.

Do not disclose a suspected vulnerability in a public Issue, Pull Request, discussion, commit, or other public channel before it has been assessed and, where appropriate, addressed. Until a private reporting channel is defined, do not submit sensitive details to this repository.

Please include the affected component or path, a concise description, reproduction steps or proof of concept, impact assessment, and any safe mitigation. Do not include secrets or personal data. Acknowledgement, triage, disclosure, and remediation timelines are `TBD`; no response or resolution SLA is promised.

## Do Not

Researchers and users must not:

- publish vulnerabilities that have not been coordinated or corrected;
- expose credentials, tokens, private keys, or personal data;
- access or alter data belonging to other users or tenants;
- perform destructive testing or delete data;
- conduct denial-of-service, load, stress, or resource-exhaustion attacks;
- conduct social engineering, phishing, or attacks against people;
- attempt physical intrusion; or
- go beyond what is necessary to demonstrate and report a vulnerability.

## Secrets

Never commit or publish tokens, GitHub App private keys, credentials, database passwords, API keys, webhook secrets, session secrets, or other sensitive authentication material in Issues, Pull Requests, logs, documentation, or the repository.

If a secret is exposed, stop using it and rotate or revoke it immediately through the responsible provider. Do not rely on deleting the file or editing history as remediation.

## Security Architecture

The planned security architecture is documented in [docs/architecture/security.md](docs/architecture/security.md). Relevant design documents also cover webhook validation, synchronization, multi-tenancy, permissions, and observability. Those documents describe plans, not a guarantee of security or compliance.

## Changes to This Policy

This policy may be updated as the project approaches private beta and public launch. Effective dates, security contact, disclosure policy, and supported versions will be added when defined.
