def detect_language(text: str) -> str:
    """Detect language for response generation"""
    if any(char in text for char in "அஆஇஈஉஊஎஏஐஒஓஔகஙசஜஞடணதநனபமயரலவழளறன"):
        return "tamil"
    hindi_keywords = ["dawa", "hospital", "mujhe", "chahiye", "sasti", "diabetes", "insulin"]
    if any(kw in text.lower() for kw in hindi_keywords):
        return "hindi"
    return "english"

def extract_state(text: str) -> str:
    mapping = {
        "chennai": "Tamil Nadu", "madurai": "Tamil Nadu", "coimbatore": "Tamil Nadu",
        "mumbai": "Maharashtra", "pune": "Maharashtra", "nagpur": "Maharashtra",
        "bangalore": "Karnataka", "mysore": "Karnataka",
        "lucknow": "Uttar Pradesh", "varanasi": "Uttar Pradesh",
        "kolkata": "West Bengal", "ahmedabad": "Gujarat"
    }
    text_lower = text.lower()
    for city, state in mapping.items():
        if city in text_lower:
            return state
    for state in ["Tamil Nadu", "Maharashtra", "Karnataka", "Uttar Pradesh", "West Bengal", "Gujarat"]:
        if state.lower() in text_lower:
            return state
    return "Tamil Nadu"