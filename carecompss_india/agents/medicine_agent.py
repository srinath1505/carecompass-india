# agents/medicine_agent.py
import json
from adk import Tool
from memory import store_result, memory
from utils import extract_state

with open('data/medicine_stores.json') as f:
    STORES = json.load(f)

# Map conditions to relevant medicines
CONDITION_MEDS = {
    "diabetes": ["Metformin", "Gliclazide", "Insulin", "Glimepiride"],
    "hypertension": ["Amlodipine", "Losartan", "Telmisartan", "Atenolol"],
    "tuberculosis": ["Rifampicin", "Isoniazid", "Ethambutol", "Pyrazinamide"],
    "anemia": ["Iron Folic Acid", "Ferrous Sulphate", "Vitamin B12"],
    "dengue": ["Paracetamol", "ORS", "Fluid"],
    "general": ["Paracetamol", "ORS"]
}

@Tool
def find_medicine(state: str, condition: str = "diabetes") -> str:
    meds_to_find = CONDITION_MEDS.get(condition, CONDITION_MEDS["general"])
    results = []
    for store in STORES:
        if store["state"] == state:
            if any(med in " ".join(store["medicines"]) for med in meds_to_find):
                results.append(f"{store['type']}: {store['name']} ({store['address']})")
    return "\n".join(results[:3]) if results else f"No medicine sources for {condition} found in {state}."

def run_medicine_agent(query: str, condition: str = "diabetes"):
    state = extract_state(query)
    result = find_medicine(state, condition)
    store_result("medicine", result)