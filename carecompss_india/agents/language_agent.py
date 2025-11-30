# agents/language_agent.py
from adk import Tool
from memory import get_result, memory
from utils import detect_language

@Tool
def format_final_response(user_query: str) -> str:
    lang = detect_language(user_query)
    memory.set("user_language", lang)
    
    meds = get_result("medicine")
    hosps = get_result("hospital")
    schemes = get_result("schemes")
    
    # Disclaimer by language
    disclaimer = {
        "english": "⚠️ Note: I am not a doctor. Please consult a physician.",
        "hindi": "⚠️ ध्यान दें: मैं डॉक्टर नहीं हूँ। कृपया चिकित्सक से परामर्श करें।",
        "tamil": "⚠️ குறிப்பு: நான் மருத்துவர் அல்ல. தயவுசெய்து மருத்துவரை கலந்தாலோசிக்கவும்."
    }.get(lang, "⚠️ Note: I am not a doctor.")
    
    # Quick Actions by language
    actions = {
        "english": "\n\n[1] Find nearest store  [2] Call helpline  [3] Book eSevai appointment",
        "hindi": "\n\n[1] निकटतम स्टोर ढूंढें  [2] हेल्पलाइन कॉल करें  [3] ई-सेवा अपॉइंटमेंट बुक करें",
        "tamil": "\n\n[1] அருகிலுள்ள கடையைக் கண்டறியவும்  [2] உதவி வரியை அழைக்கவும்  [3] ஈ-சேவை நேரம் பதிவு செய்யவும்"
    }
    
    return f"{meds}\n\n{hosps}\n\n{schemes}\n\n{disclaimer}{actions.get(lang, actions['english'])}"