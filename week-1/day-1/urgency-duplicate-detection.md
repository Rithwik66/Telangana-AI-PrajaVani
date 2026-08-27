# Telangana AI–PrajaVani

## Day 1 — Urgency and Duplicate Detection

### 1. Urgency Identification

Urgency identification determines how quickly a citizen grievance may need attention.

The AI system should examine the complaint and assign an appropriate urgency level based on the information provided.

#### Suggested Urgency Levels

- **High** — Issues that may require immediate or priority attention.
- **Medium** — Issues that require timely action but are not immediately critical.
- **Low** — General complaints or requests that can follow the normal processing workflow.

### 2. Why Urgency Matters

Identifying urgency helps government grievance systems prioritize complaints and focus attention on cases that may require faster action.

The urgency field can therefore support:

- Complaint prioritization
- Faster routing
- Better workload management
- Identification of potentially critical grievances

### 3. Duplicate Detection

Citizens may submit multiple complaints describing the same or a very similar issue.

The system should identify possible duplicate complaints by comparing relevant information such as:

- Complaint text
- Location
- Department
- Category
- Issue description
- Other available complaint information

### 4. Why Duplicate Detection Matters

Duplicate detection can help reduce repeated processing of the same grievance and provide a clearer view of the actual number of distinct issues being reported.

Possible duplicate complaints should be flagged for review rather than automatically discarded.

### 5. Processing Flow

Citizen Complaint
        ↓
Analyze Complaint
        ↓
Determine Urgency
        ↓
Check for Similar Complaints
        ↓
Flag Possible Duplicate
        ↓
Continue Grievance Processing

### Expected Outcome

Urgency identification and duplicate detection provide two important signals for grievance prioritization and processing. These fields can later be incorporated into the AI-assisted grievance classification and routing workflow.