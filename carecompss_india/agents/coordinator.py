# agents/coordinator.py
from agents.medicine_agent import run_medicine_agent
from agents.hospital_agent import run_hospital_agent
from agents.schemes_agent import run_schemes_agent
from agents.language_agent import format_final_response
from features.symptom_mapper import infer_condition_from_query
from memory import memory

class CoordinatorAgent:
    @staticmethod
    def process_query(user_query: str) -> str:
        # Infer condition from symptoms
        condition = infer_condition_from_query(user_query)
        memory.set("user_condition", condition)
        print(f"🩺 Detected condition: {condition}")  # For debugging
        
        # Run specialized agents
        run_medicine_agent(user_query, condition=condition)
        run_hospital_agent(user_query, condition=condition)
        run_schemes_agent(user_query)
        
        # Generate final response with actions
        return format_final_response(user_query)

Coordinator = CoordinatorAgent()