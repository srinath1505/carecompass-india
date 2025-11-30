# agents/schemes_agent.py
import json
from adk import Tool
from memory import store_result
from utils import extract_state

with open('data/state_health_schemes.json') as f:
    SCHEMES = json.load(f)

@Tool
def get_schemes(state: str) -> str:
    for item in SCHEMES:
        if item["state"] == state:
            resp = f"State health schemes in {state}:\n"
            for s in item["schemes"]:
                name = s.get("name", "Scheme")
                coverage = s.get("coverage_amount", "Details not available")
                apply_info = s.get("how_to_apply", "Visit local health center")
                resp += f"- {name}:\n  • Coverage: {coverage}\n  • Apply: {apply_info}\n"
            return resp
    return f"No state schemes found for {state}."

def run_schemes_agent(query: str):
    state = extract_state(query)
    result = get_schemes(state)
    store_result("schemes", result)