import json
from urgency_scorer import calculate_urgency

def process_grievance(grievance_text: str) -> dict:
    # 1. Calculate urgency
    urgency_data = calculate_urgency(grievance_text)
    
    # 2. Mock routing based on taxonomy rules
    # (In full system, this connects to day-4 department_classifier.pkl)
    department = "electricity" if "wire" in grievance_text.lower() or "sparking" in grievance_text.lower() else "municipal"
    
    return {
        "text": grievance_text,
        "assigned_department": department,
        "urgency_score": urgency_data["urgency_score"],
        "explainable_factor": urgency_data["explainable_factor"]
    }

if __name__ == "__main__":
    sample = "Live wire fallen on the main road causing sparking"
    result = process_grievance(sample)
    print(json.dumps(result, indent=2))
