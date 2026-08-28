# Telangana AI–PrajaVani

## Day 2 — API Contract

### Purpose

The API contract defines the minimum interfaces required for the Telangana AI–PrajaVani system. It provides a common structure for complaint creation, classification, duplicate checking, scheme search, case lookup, and dashboard analytics.

### API Endpoints

| Method | Endpoint | Purpose | Minimum Fields |
|---|---|---|---|
| POST | `/complaints` | Create complaint from text or voice | text/audio, language, location, citizen_channel |
| POST | `/classify` | Predict category and department | normalized_text |
| POST | `/duplicate-check` | Find similar complaints | text, location, time_window |
| POST | `/schemes/search` | Retrieve relevant scheme documents | query, optional profile attributes |
| GET | `/complaints/{id}` | Get case status | complaint_id |
| GET | `/dashboard/summary` | Officer analytics | filters |

### Classification API

#### Request

The classification module accepts:

- `normalized_text`
- Optional `language`
- Optional `location` context

#### Response

The classification response should provide:

- `category`
- `department`
- `urgency_score`
- `confidence`

### Duplicate-Check API

#### Request

The duplicate-check module accepts:

- `text`
- Optional `location`
- `time_window`
- Prior complaint reference set

#### Response

The response should provide:

- `duplicate_score`
- `duplicate_group` or linked candidate
- `confidence`

### Duplicate Detection Approach

Duplicate detection should use semantic similarity rather than exact keyword matching.

Location information such as ward, mandal or pincode can be used as an additional constraint. A suitable time window can also help distinguish an ongoing incident from an unrelated historical complaint.

### API Design Principles

1. Use consistent field names across modules.
2. Keep module inputs and outputs explicit.
3. Match department, category and urgency outputs with the Day 1 taxonomy.
4. Provide confidence information where applicable.
5. Keep the API contract suitable for integration with other project modules.

### Expected Outcome

The API contract provides a clear interface between the grievance intake, classification, urgency, duplicate detection, knowledge retrieval, and backend components. 