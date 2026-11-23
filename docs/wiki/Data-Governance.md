# Data Governance

**Status:** Proposed control model; data inventory not yet completed.

## Mandatory data-domain record

For every domain, record:
- Business owner and technical custodian.
- Purpose and approved use.
- Source of truth.
- Data subjects and categories.
- Classification and sensitivity.
- Access roles and approval process.
- Quality and reconciliation rules.
- Retention and deletion rules.
- Export, backup and recovery procedure.
- Processors, recipients and integration endpoints.

## Classification

| Level | Examples | Minimum handling |
|---|---|---|
| Public | Approved public marketing copy | Accuracy and publication approval |
| Internal | Non-sensitive operating procedures | Staff access as needed |
| Confidential | Business plans, customer records, contracts | Role-based access and controlled sharing |
| Restricted | Credentials, private keys and sensitive security records | Strong controls; secrets outside ordinary records and source control |

## Source of truth

Every critical field must have a declared authoritative source. Replicas must retain source IDs and timestamps. Reconciliation failures must create an owned exception.

Airtable may be an operational workflow layer for approved Invest records. It must not replace banking, regulated custody, payment or statutory accounting systems.

## Data lifecycle

Collect for an identified purpose, validate, classify, authorise, use, retain only as needed, then archive or delete under an approved schedule.

Where GDPR applies, document purpose, lawful basis, transparency, minimisation, accuracy, retention, rights handling and safeguards.

## Prohibited repository content

Never commit passwords, private keys, recovery phrases, API tokens, payment-card data, personal documents or real customer datasets.

See [Data Governance Standard](../DATA_GOVERNANCE.md).
