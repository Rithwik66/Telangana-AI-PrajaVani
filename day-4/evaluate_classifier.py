import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    f1_score,
    classification_report,
    confusion_matrix
)

# Load dataset
data = pd.read_csv("data/grievances.csv")

X = data["text"]
y = data["department"]

# Use the same split as training
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

# Load trained classifier
model = joblib.load("models/department_classifier.joblib")

# Predict
y_pred = model.predict(X_test)

# Metrics
accuracy = accuracy_score(y_test, y_pred)
macro_f1 = f1_score(y_test, y_pred, average="macro")

print("\n===== Classifier v1 Evaluation =====")
print(f"Accuracy: {accuracy:.2f}")
print(f"Macro F1: {macro_f1:.2f}")

print("\n===== Classification Report =====")
print(classification_report(y_test, y_pred))

print("\n===== Confusion Matrix =====")
print(confusion_matrix(y_test, y_pred)) 