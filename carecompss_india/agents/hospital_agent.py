# agents/hospital_agent.py
import json
from adk import Tool
from memory import store_result
from utils import extract_state

with open('data/pmjay_hospitals.json') as f:
    HOSPITALS = json.load(f)

# Map conditions to relevant hospital services
CONDITION_SERVICES = {
    "diabetes": ["Diabetes", "Endocrinology", "Sugar"],
    "hypertension": ["Cardiology", "BP", "Hypertension"],
    "tuberculosis": ["TB", "DOTS", "Respiratory", "Chest"],
    "anemia": ["Hematology", "Blood", "Nutrition"],
    "dengue": ["Fever", "Infectious", "Medicine"],
    "general": ["General Medicine"]
}

@Tool
def find_hospitals(state: str, condition: str = "diabetes") -> str:
    services = CONDITION_SERVICES.get(condition, CONDITION_SERVICES["general"])
    results = []
    for hosp in HOSPITALS:
        if hosp["state"] == state and hosp["pmjay_empaneled"]:
            hosp_services = " ".join(hosp["services"])
            if any(svc.lower() in hosp_services.lower() for svc in services):
                results.append(f"{hosp['hospital']} - {', '.join(hosp['services'])}")
    return "\n".join(results[:2]) if results else f"No PMJAY hospitals for {condition} in {state}."

def run_hospital_agent(query: str, condition: str = "diabetes"):
    state = extract_state(query)
    result = find_hospitals(state, condition)
    store_result("hospital", result)