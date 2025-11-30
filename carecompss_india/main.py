# main.py
from agents.coordinator import Coordinator
from agents.reminder_agent import create_care_reminder

# Test queries covering all key features
QUERIES = [
    # Diabetes query (Hindi)
    "Mujhe Chennai mein diabetes ki sasti dawa chahiye.",
    
    # TB symptom query (Hindi - shows advanced reasoning)
    "Mujhe 3 hafte se khaansi hai aur raat ko bukhar aata hai.",
    
    # Anemia symptom query (English)
    "I feel very tired, pale, and weak all the time.",
    
    # Dengue symptom query (Tamil)
    "எனக்கு அதிக காய்ச்சல், தீவிர தலைவலி மற்றும் மூட்டு வலி உள்ளது.",
    
    # General query (English)
    "I need affordable insulin in Pune."
]

if __name__ == "__main__":
    for i, q in enumerate(QUERIES, 1):
        print(f"\n{'='*80}")
        print(f"TEST CASE {i}: '{q}'")
        print(f"\n{' CARECOMPASS INDIA - Multi-Agent Health Concierge ':=^80}")
        
        # Get main response from coordinator
        response = Coordinator.process_query(q)
        print(f"\n💡 ASSISTANCE:\n{response}")
        
        # Get personalized follow-up reminder
        reminder = create_care_reminder()
        print(f"\n🔔 FOLLOW-UP REMINDER:\n{reminder}")
        
        print(f"\n{'='*80}")