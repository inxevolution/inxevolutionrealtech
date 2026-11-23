# In X Evolution — Security, Privacy and Quality Baseline

**Version:** 0.2  
**Date:** 23 November 2026  
**Status:** Control baseline — applicability and implementation review required

## 1. Purpose

This document establishes minimum controls for future In X Evolution products and operations. It is not a certification, legal opinion or statement that the controls have already been implemented.

## 2. Portfolio-specific trust boundaries

In X Evolution is considering multiple business lines: Real Technology, Invest, SHOP and community. They may share selected enterprise capabilities, but must not automatically share all records or access rights.

- Technology client code, data and credentials are confidential to the authorised delivery team.
- Invest research and internal records must be distinguished from customer assets and third-party account credentials.
- SHOP customer, order and payment references must be restricted to operational roles.
- Community membership and communication data must not become a general marketing list without an appropriate basis and user information.
- Shared management reporting should use the minimum data necessary.

## 3. Secure development baseline

### Identity and access
- Individual identities for privileged access.
- Least privilege and role separation.
- Strong authentication, including MFA for privileged access where supported.
- Periodic permission reviews and prompt removal of obsolete access.
- No shared passwords or access tokens.

### Secrets and configuration
- Never commit passwords, API keys, private keys, wallet seed phrases, recovery codes or production tokens.
- Store secrets in an approved secret manager or protected environment configuration.
- Rotate exposed credentials and investigate possible misuse.
- Keep development, test and production configuration separate.

### Application security
- Validate untrusted input on the server side.
- Use safe query construction and context-appropriate output encoding.
- Enforce authorisation at every protected operation.
- Use secure session and token handling.
- Apply rate limits and abuse controls where appropriate.
- Maintain dependencies and assess security advisories.
- Avoid logging secrets, full payment data or unnecessary personal information.

### Operations
- Restrict network exposure and administrative interfaces.
- Patch supported operating systems, runtimes and dependencies.
- Define backup, restore and incident procedures before production.
- Test recovery rather than merely assuming backups work.

## 4. Privacy baseline

Before personal data processing, document data subjects, categories, purposes, lawful basis, recipients, processors, transfers, retention, deletion, data-subject rights and security measures.

Apply the GDPR principles where the Regulation applies: lawfulness, fairness, transparency, purpose limitation, data minimisation, accuracy, storage limitation, integrity/confidentiality and accountability. Implement privacy by design and by default.

Reference: [European Commission — Principles of the GDPR](https://commission.europa.eu/law/law-topic/data-protection/information-business-and-organisations/principles-gdpr_en).

## 5. Financial and regulated-activity safeguards

The word “Invest” or public links to investment platforms do not establish permission to provide financial services.

Before any Invest offer is published or delivered, classify the exact activity and obtain qualified legal review where required. Distinguish:
- General factual or educational information.
- Advertising, referrals and affiliate marketing.
- Personalised investment recommendations.
- Reception/transmission or execution of orders.
- Portfolio management, custody or control of customer assets.
- Payment or electronic-money services.
- Crypto-asset services and other potentially regulated activities.

Do not offer regulated activities unless the legal entity, jurisdiction, authorisation and operating arrangements have been confirmed. Verify counterparties and disclose material conflicts and commercial relationships. Do not promise returns or treat mining rewards or token values as guaranteed.

Useful official checks for Portugal:
- [CMVM — Authorised entities](https://investidor.cmvm.pt/PInvestidor/Content?Input=07D419590495176787CBC8290D95B30F1235C4ACE874EA8E408B180D23294F55&_ts=1720828800034)
- [Banco de Portugal — Institutions and authorised activities](https://clientebancario.bportugal.pt/pt-pt/instituicoes)

These references do not determine the classification of In X Evolution's activities; obtain advice based on the actual service.

## 6. Commerce and partner safeguards

For SHOP and any affiliate offer:
- Identify seller of record and responsible service provider.
- Confirm accurate product information, total price, taxes and delivery terms.
- Define returns, refunds, warranty and support responsibility.
- Disclose sponsorship and affiliate relationships.
- Verify partner identity, contract, data access and complaint escalation.
- Do not imply third-party endorsement or ownership without evidence.

## 7. Secure engineering lifecycle

1. Identify assets, actors, abuse cases and trust boundaries.
2. Define security and privacy requirements.
3. Review design, providers and dependencies.
4. Implement controls with peer review.
5. Test positive, negative, boundary and permission cases.
6. Scan dependencies and source where appropriate.
7. Review deployment configuration and secrets.
8. Monitor, patch and respond to findings.

## 8. Testing strategy

| Test type | Purpose |
|---|---|
| Unit | Verify isolated business rules, calculations and validation |
| Integration | Verify database, identity and third-party boundaries |
| E2E | Verify priority customer and operator journeys |
| Security | Verify authentication, authorisation, input safety and secret handling |
| Data reconciliation | Verify finance, mining and integration records against their authoritative source |
| Performance | Verify behaviour under agreed workloads |
| Accessibility | Evaluate inclusive interaction in user-facing interfaces |
| Recovery | Verify backup restoration and documented recovery processes |

Tests must be repeatable and linked to requirements.

## 9. Release-readiness checklist

- [ ] Requirements and acceptance criteria approved.
- [ ] Code reviewed and required tests passing.
- [ ] No unresolved critical/high issue without authorised risk acceptance.
- [ ] Secrets and configuration checked.
- [ ] Personal data and financial activity reviewed.
- [ ] Provider integrations and permissions verified.
- [ ] Migrations and rollback/recovery assessed.
- [ ] Monitoring and support owner defined.
- [ ] Documentation and user-facing disclosures updated.

## 10. Incident handling

An operational runbook must define severity, contacts, containment, evidence preservation, recovery, communications, privacy/legal escalation and post-incident review.

Report suspected vulnerabilities privately. Do not publish credentials, exploit details or sensitive customer evidence in public repository issues.
