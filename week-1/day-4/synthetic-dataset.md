# Telangana AI–PrajaVani

## Day 4 — Synthetic Grievance Dataset v1

### Purpose

The Day 4 task is to create a small, safe, synthetic grievance dataset for testing the Department Routing, Urgency Scoring, and Duplicate Detection modules.

The dataset uses fictional examples and does not contain real citizen personal information.

### Dataset Fields

Each synthetic grievance should contain:

| Field | Description |
|---|---|
| complaint_id | Unique identifier |
| language | Telugu, English, or Tanglish |
| raw_text | Synthetic citizen complaint |
| normalized_text | Normalized complaint text |
| department | Expected department |
| category | Complaint category |
| urgency_score | Expected urgency from 1 to 5 |
| location | Example locality |
| duplicate_group | Duplicate group when applicable |

### Synthetic Grievance Examples

| ID | Language | Complaint | Department | Category | Urgency | Location | Duplicate Group |
|---|---|---|---|---|---:|---|---|
| SG001 | English | There is a large pothole near the main bus stop and vehicles are struggling to pass. | Roads / transport | Roads / infrastructure | 4 | Hanamkonda | DG001 |
| SG002 | Tanglish | Hanamkonda bus stop daggara pedda pothole undi, vehicles ki problem avutundi. | Roads / transport | Roads / infrastructure | 4 | Hanamkonda | DG001 |
| SG003 | Telugu | మా ప్రాంతంలో తాగునీటి సరఫరా సక్రమంగా లేదు. | Water supply | Water supply | 3 | Warangal | DG002 |
| SG004 | English | The street lights in our locality have not been working for several days. | Municipal / GHMC-type civic services | Civic services | 3 | Hyderabad | DG003 |
| SG005 | Tanglish | Maa area lo street lights work avvatledu. | Municipal / GHMC-type civic services | Civic services | 3 | Hyderabad | DG003 |
| SG006 | English | I have not received the eligible welfare pension payment. | Public health | Welfare / service delivery | 3 | Karimnagar | — |
| SG007 | Telugu | మా భూమికి సంబంధించిన రెవెన్యూ రికార్డులో సమస్య ఉంది. | Revenue / land administration | Land / revenue | 3 | Nalgonda | — |
| SG008 | English | There is an exposed electrical wire near a residential street. | Electricity / power utility | Electrical safety | 5 | Khammam | — |
| SG009 | Tanglish | School ki velladaniki road chala damage ayyindi. | Roads / transport | Roads / infrastructure | 3 | Siddipet | — |
| SG010 | Telugu | మా గ్రామంలో చెత్త సేకరణ సక్రమంగా జరగడం లేదు. | Sanitation / solid waste | Sanitation | 3 | Suryapet | — |

### Duplicate Pair Examples

#### Duplicate Group DG001

**SG001**

> There is a large pothole near the main bus stop and vehicles are struggling to pass.

**SG002**

> Hanamkonda bus stop daggara pedda pothole undi, vehicles ki problem avutundi.

These complaints describe the same underlying issue and locality using different language styles. They should therefore receive a high duplicate probability.

#### Duplicate Group DG003

**SG004**

> The street lights in our locality have not been working for several days.

**SG005**

> Maa area lo street lights work avvatledu.

These complaints describe the same type of civic issue in the same locality and can be linked as a duplicate candidate.

### Non-Duplicate Example

A similar complaint type should not automatically be treated as a duplicate when the location is different.

Example:

- Huge pothole near Hanamkonda bus stand.
- Huge pothole near Warangal railway station.

The complaint type is similar, but the different location means the cases should not automatically be linked.

### Urgency Examples

| Urgency | Example |
|---:|---|
| 1 | General information request with no immediate issue |
| 2 | Routine service request |
| 3 | Moderate civic or service issue affecting citizens |
| 4 | Significant issue requiring quick attention |
| 5 | Serious safety risk requiring immediate or priority attention |

### Dataset Design Principles

1. Use synthetic complaints only.
2. Include Telugu, English, and Tanglish examples.
3. Include examples across the target government departments.
4. Include both duplicate and non-duplicate examples.
5. Include different urgency levels.
6. Keep the expected department and urgency labels explicit.
7. Do not include real citizen names, phone numbers, addresses, or other personal information.

### Intended Use

The dataset can be used for:

- Department routing evaluation
- Urgency scoring evaluation
- Duplicate detection testing
- API testing
- Future model evaluation
- Demonstration and development

### Expected Outcome

Dataset v1 provides a safe synthetic evaluation set for testing the Department Routing, Urgency Scoring, and Duplicate Detection modules before using real citizen grievance data. 