# Telangana AI–PrajaVani

## Day 1 — Dataset Fields

### Purpose

The dataset fields define the information that should be captured from each citizen grievance. A clear and consistent dataset structure is required so that complaints can be analyzed, classified, routed, prioritized, and evaluated by the AI system.

### Core Dataset Fields

| Field | Description |
|---|---|
| Complaint ID | Unique identifier for each grievance |
| Complaint Text | Original complaint submitted by the citizen |
| Department | Government department responsible for the issue |
| Category | Category representing the type of grievance |
| Urgency | Priority level such as High, Medium, or Low |
| Location | Location associated with the grievance |
| Status | Current processing status of the complaint |
| Duplicate Indicator | Indicates whether the complaint may be a duplicate |
| Date/Time | Date and time when the grievance was submitted |
| Source | Channel or source through which the grievance was received |

### Success Metrics

The success metrics define how the effectiveness of the grievance AI system can be evaluated.

| Metric | Purpose |
|---|---|
| Department Classification Accuracy | Measures whether complaints are assigned to the correct department |
| Category Classification Accuracy | Measures the correctness of grievance category classification |
| Urgency Classification Accuracy | Measures how accurately urgency levels are identified |
| Duplicate Detection Performance | Measures the ability to identify similar or duplicate grievances |
| Structured Field Completeness | Measures how consistently required information is extracted |
| Routing Accuracy | Measures whether grievances reach the appropriate department or authority |
| Processing Efficiency | Measures improvement in grievance processing workflow |

### Dataset Design Principles

The dataset should be:

- **Structured** — important information should be represented using consistent fields.
- **Clear** — each field should have a defined purpose.
- **Consistent** — values should follow standard formats where possible.
- **Traceable** — each grievance should have a unique identifier.
- **Expandable** — additional fields can be added as the system develops.

### Expected Outcome

The Day 1 dataset design establishes the information required for the AI-assisted grievance understanding and routing workflow. It provides the foundation for the detailed data schema and API contract developed in later tasks.
