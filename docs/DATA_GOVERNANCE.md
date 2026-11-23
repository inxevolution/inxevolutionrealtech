# In X Evolution — Data Governance Standard

**Version:** 0.1 · **Status:** Proposed.

## Objective

Make data ownership, quality, access, retention and reconciliation explicit across the portfolio.

## Mandatory data-domain record

For each domain, record owner, custodian, purpose, source of truth, subjects/categories, classification, access roles, quality rules, retention/deletion, export/recovery, processors and integrations.

## Classification

| Level | Examples | Minimum handling |
|---|---|---|
| Public | Approved marketing copy | Accuracy and publication approval |
| Internal | Non-sensitive operating procedures | Staff access as needed |
| Confidential | Business plans, customer records, contracts | Role-based access and controlled sharing |
| Restricted | Credentials, private keys, sensitive security records | Strong controls; secrets outside ordinary records/source control |

## Source-of-truth rules

Every critical field must have an authoritative source. Replicas must retain source IDs and timestamps. Reconciliation failures create an exception with an owner.

Airtable may support approved Invest operations. It must not be assumed to replace banking, regulated custody, payments or statutory accounting systems.

## Data lifecycle

Collect for an identified purpose, validate, classify, authorise, use, retain only as needed, then archive or delete under an approved schedule.

Where GDPR applies, document purpose, lawful basis, transparency, minimisation, accuracy, retention, rights handling and safeguards.

## Prohibited repository content

Never commit passwords, private keys, recovery phrases, API tokens, payment-card data, personal documents or real customer datasets.

## Airtable safeguards

Preserve the three Mining records identified by the project owner. Before material schema changes, export or otherwise safeguard records, test changes non-destructively, reconcile IDs and values, and obtain explicit confirmation before deleting or overwriting data.
