# Telangana AI–PrajaVani

## Week 2 — Day 1
## Classifier Dataset

### Objective

Prepare a labeled dataset for the baseline department and category classifier.

The dataset uses the taxonomy established during Week 1 and provides expected labels that can later be used for training and evaluation.

### Dataset Fields

| Field | Description |
|---|---|
| complaint_id | Unique complaint identifier |
| language | Telugu, English, or Tanglish |
| raw_text | Original complaint text |
| normalized_text | Cleaned/normalized complaint text |
| category | Expected complaint category |
| department | Expected department |
| urgency_score | Expected urgency from 1–5 |

### Labeled Examples

| ID | Language | Complaint | Category | Department | Urgency |
|---|---|---|---|---|---:|
| C001 | English | There is a large pothole near the bus stop. | Roads / infrastructure | Roads / transport | 4 |
| C002 | Tanglish | Maa area lo street lights work avvatledu. | Civic services | Municipal / GHMC-type civic services | 3 |
| C003 | Telugu | మా ప్రాంతంలో తాగునీటి సరఫరా సక్రమంగా లేదు. | Water supply | Water supply | 3 |
| C004 | English | There is an exposed electrical wire near houses. | Electrical safety | Electricity / power utility | 5 |
| C005 | English | I have not received my eligible welfare pension. | Welfare / service delivery | Public health | 3 |
| C006 | Telugu | మా భూమికి సంబంధించిన రెవెన్యూ రికార్డులో సమస్య ఉంది. | Land / revenue | Revenue / land administration | 3 |
| C007 | Tanglish | School ki velladaniki road chala damage ayyindi. | Roads / infrastructure | Roads / transport | 3 |
| C008 | English | Garbage collection is not happening regularly in our locality. | Sanitation | Sanitation / solid waste | 3 |
| C009 | Tanglish | Bus stop daggara road lo pedda pothole undi. | Roads / infrastructure | Roads / transport | 4 |
| C010 | English | The water supply has been disrupted in our locality. | Water supply | Water supply | 3 |

### Labeling Rules

1. Every complaint must have an expected department.
2. Every complaint must have an expected category.
3. Urgency must use the 1–5 scale established in Week 1.
4. Telugu, English, and Tanglish inputs should be represented.
5. Labels should be consistent with the Week 1 taxonomy.
6. Synthetic data should be used for development and testing.
7. Real citizen personal information must not be included.

### Dataset Split

The dataset should eventually be separated into:

- Training data
- Validation data
- Test data

The test set should remain separate from training data so that classifier performance can be evaluated fairly.

### Class Balance

The dataset should be checked for significant imbalance between departments and categories.

If one department has substantially more examples than another, additional examples should be collected or generated before training.

### Evaluation Metrics

The classifier will later be evaluated using:

- Precision
- Recall
- F1 score
- Confusion matrix
- Department-routing Macro F1

The Week 1 MVP target for department routing is:

**Macro F1 ≥ 80%**

### Expected Outcome

A labeled and consistently structured dataset is prepared for training and evaluating the baseline department/category routing classifier.
