# Telangana AI–PrajaVani

## Day 4 — Dataset Validation

### Validation Checklist

- [ ] Dataset contains synthetic grievance examples.
- [ ] Telugu, English, and Tanglish examples are included.
- [ ] Target government departments are represented.
- [ ] Complaint categories are assigned.
- [ ] Urgency scores from 1 to 5 are represented.
- [ ] Duplicate complaint pairs are included.
- [ ] Non-duplicate examples are included.
- [ ] Location information is available for duplicate comparison.
- [ ] Duplicate groups are identified where applicable.
- [ ] No real citizen personal information is included.

### Department Routing Validation

Each synthetic complaint should have an expected department label.

The labels provide the reference values required to evaluate the Department Routing module.

### Urgency Scoring Validation

Each complaint contains an expected urgency score from 1 to 5.

The examples provide labeled cases that can later be used to compare model predictions against expected urgency levels.

### Duplicate Detection Validation

Duplicate groups provide positive examples for duplicate detection.

Non-duplicate examples provide negative cases where similar complaint types should not automatically be linked because the underlying incident or locality differs.

### Evaluation Approach

The dataset can later be divided into development and evaluation examples.

For Department Routing:

**Predicted Department → Compare with Expected Department**

For Urgency Scoring:

**Predicted Score → Compare with Expected Score**

For Duplicate Detection:

**Predicted Duplicate Relationship → Compare with Expected Duplicate Group**

### Data Safety

This dataset is synthetic and is intended only for development, testing, demonstration, and evaluation.

Real citizen names, phone numbers, addresses, or other personally identifying information must not be added to this dataset.

### Expected Outcome

The validated Dataset v1 provides labeled synthetic examples that can be used to test and evaluate the Department Routing, Urgency Scoring, and Duplicate Detection modules. 