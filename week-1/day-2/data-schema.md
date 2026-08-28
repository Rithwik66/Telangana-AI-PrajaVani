# Telangana AI–PrajaVani

## Day 2 — Data Schema

### Purpose

The Day 2 data schema defines the common structure for a citizen grievance. It provides a shared contract that can later connect language processing, classification, urgency scoring, duplicate detection, and the backend.

### Common Complaint Record

| Field | Purpose |
|---|---|
| complaint_id | Unique complaint/case identifier |
| language | Detected language or input style such as Telugu, English or Tanglish |
| raw_text | Original citizen-submitted complaint |
| normalized_text | Normalized representation used by downstream models |
| category | Fine-grained complaint category |
| department | Recommended department label |
| urgency_score | Priority score from 1 to 5 |
| location | Available locality, ward, mandal or pincode information |
| duplicate_group | Identifier for a set of related or duplicate complaints |

### Urgency Field

The urgency score is an integer from 1 to 5.

| Score | Working Interpretation |
|---|---|
| 1 | Very low priority / information-type or non-urgent issue |
| 2 | Low priority routine complaint |
| 3 | Moderate issue affecting citizens without immediate danger |
| 4 | High priority issue requiring quick action |
| 5 | Critical or emergency issue involving serious safety risk |

### Duplicate Detection Fields

Duplicate detection requires information that can help compare a complaint with previous complaints.

Important inputs include:

- Complaint text
- Location
- Time window
- Prior complaint reference set

Duplicate detection should use semantic similarity rather than exact keyword matching.

Location information such as ward, mandal or pincode can provide an additional locality constraint. A suitable time window can also help distinguish an ongoing incident from an unrelated historical complaint.

### Schema Design Principles

1. All common field names should remain fixed and documented.
2. Department, category and urgency outputs should match the Day 1 taxonomy.
3. Location and duplicate fields should be available for duplicate detection.
4. Module inputs and outputs should be explicit.
5. The schema should be usable as a common contract by other project modules.

### Expected Outcome

The Day 2 schema provides the common structure required for the project's AI modules and backend integration. 