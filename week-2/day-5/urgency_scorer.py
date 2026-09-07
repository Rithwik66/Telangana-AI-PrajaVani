import re

def calculate_urgency(text: str) -> dict:
    text_lower = text.lower()
    
    critical_keywords = ["sparking", "fire", "accident", "injury", "collapse", "live wire", "sewage leak", "emergency"]
    high_keywords = ["pothole", "no power", "outage", "dirty water", "overflowing", "theft", "threat"]
    moderate_keywords = ["leak", "power cut", "no water", "garbage", "street light", "delayed"]
    
    if any(re.search(rf"\b{kw}\b", text_lower) for kw in critical_keywords):
        return {"urgency_score": 5, "explainable_factor": "Critical safety hazard or acute emergency detected."}
    elif any(re.search(rf"\b{kw}\b", text_lower) for kw in high_keywords):
        return {"urgency_score": 4, "explainable_factor": "High priority public infrastructure or utility issue."}
    elif any(re.search(rf"\b{kw}\b", text_lower) for kw in moderate_keywords):
        return {"urgency_score": 3, "explainable_factor": "Standard civic grievance requiring routine department action."}
    else:
        return {"urgency_score": 2, "explainable_factor": "General administrative or low-severity inquiry."}

if __name__ == "__main__":
    sample = "Live wire fallen on the main road causing sparking"
    print("Test Output:", calculate_urgency(sample))
