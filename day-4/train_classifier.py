import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, classification_report


# Load dataset
data = pd.read_csv("data/grievances.csv")

# Input and target
X = data["text"]
y = data["department"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

# Create TF-IDF + Logistic Regression pipeline
model = Pipeline([
    ("tfidf", TfidfVectorizer(
        lowercase=True,
        ngram_range=(1, 2)
    )),
    ("classifier", LogisticRegression(
        max_iter=1000
    ))
])

# Train model
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Metrics
accuracy = accuracy_score(y_test, y_pred)
macro_f1 = f1_score(y_test, y_pred, average="macro")

print("\n===== Telangana AI–PrajaVani Classifier v1 =====")
print(f"Accuracy: {accuracy:.2f}")
print(f"Macro F1: {macro_f1:.2f}")

print("\n===== Classification Report =====")
print(classification_report(y_test, y_pred))

# Save trained model
joblib.dump(model, "models/department_classifier.joblib")

print("\nModel saved to:")
print("models/department_classifier.joblib") 