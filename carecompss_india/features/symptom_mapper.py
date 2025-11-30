# features/symptom_mapper.py

SYMPTOM_KEYWORDS = {
    # Diabetes
    "diabetes": [
        # English
        "thirsty", "urinate often", "frequent urination", "tired", "fatigue", "weight loss", 
        "blurry vision", "slow healing", "numbness", "tingling", "sugar", "diabetes", "high sugar",
        # Hindi (Romanized)
        "pyaas", "baar baar peshab", "thakavat", "kamzori", "vajan kam", "dhrishti dhundhla",
        "chot dheere bharo", "sui jaisa dard", "madhumeh",
        # Tamil
        "தாகம்", "அடிக்கடி சிறுநீர்", "சோர்வு", "எடை குறைவு", "பார்வை மங்கல்", "ஆரோக்கியமாக குணமடையாமல்",
        "உணர்விழப்பு", "சர்க்கரை", "நீரிழிவு"
    ],
    
    # Hypertension (High BP)
    "hypertension": [
        # English
        "headache", "dizziness", "chest pain", "shortness of breath", "nosebleed", "bp high", 
        "high blood pressure", "palpitations", "vision changes",
        # Hindi
        "sir dard", "chakkar", "chehre ka dard", "saans phoolna", "nak se khoon", "bp zyada",
        "dil ki dhadkan", "dhrishti badalna",
        # Tamil
        "தலைவலி", "மயக்கம்", "மார்பு வலி", "மூச்சுத் திணறல்", "மூக்கு இரத்தப்போக்கு", "இரத்த அழுத்தம் அதிகம்",
        "இதயத் துடிப்பு", "பார்வை மாற்றம்"
    ],
    
    # Tuberculosis (TB) – High burden in India
    "tuberculosis": [
        # English
        "cough more than 2 weeks", "cough blood", "fever at night", "night sweats", 
        "weight loss", "loss of appetite", "chest pain", "tb", "tuberculosis",
        # Hindi
        "2 hafte se zyada khaansi", "khaansi mein khoon", "raat ko bukhar", "raat ko paseena",
        "bhookh nahi lagana", "madhumeh", "chehre ka dard",
        # Tamil
        "2 வாரத்திற்கு மேல் இருமல்", "இரத்தத்துடன் இருமல்", "இரவு காய்ச்சல்", "இரவு வியர்வை",
        "பசி இல்லாமல் போதல்", "எடை குறைவு", "மார்பு வலி", "காசநோய்"
    ],
    
    # Anemia (Common in Indian women)
    "anemia": [
        # English
        "pale skin", "weakness", "fatigue", "shortness of breath", "dizziness", "cold hands",
        "irregular heartbeat", "anemia", "low hemoglobin",
        # Hindi
        "chehra safed", "kamzori", "thakavat", "saans phoolna", "chakkar", "haath pair thande",
        "dil ki dhadkan be-tartib", "khuni kami", "hemoglobin kam",
        # Tamil
        "வெளிர் தோல்", "பலவீனம்", "சோர்வு", "மூச்சுத் திணறல்", "மயக்கம்", "கைகால்கள் குளிர்ச்சி",
        "இதயத் துடிப்பு ஒழுங்கற்றது", "இரத்தச் சோகை", "ஹீமோக்லோபின் குறைவு"
    ],
    
    # Dengue (Seasonal, India-prevalent)
    "dengue": [
        # English
        "high fever", "severe headache", "pain behind eyes", "joint pain", "rash", 
        "bleeding gums", "low platelets", "dengue",
        # Hindi
        "tez bukhar", "tez dard", "aankhon ke peeche dard", "joints dard", "daanay",
        "mooth se khoon", "platelets kam", "dengue",
        # Tamil
        "அதிக காய்ச்சல்", "தீவிர தலைவலி", "கண்களுக்குப் பின்னால் வலி", "மூட்டு வலி", "தடிப்பு",
        "பல் வாயிலிருந்து இரத்தம்", "பிளேட்லெட்கள் குறைவு", "டெங்கு"
    ],
    
    # General fallback
    "general": [
        "hospital", "doctor", "medicine", "dawai", "treatment", "ilaj", "dawa", "marunthu", "vaithiyar"
    ]
}

def infer_condition_from_query(query: str) -> str:
    """Map user query to medical condition using symptom keywords"""
    query_lower = query.lower()
    
    # Check specific conditions in order of severity
    for condition in ["tuberculosis", "dengue", "diabetes", "hypertension", "anemia"]:
        if any(kw in query_lower for kw in SYMPTOM_KEYWORDS[condition]):
            return condition
    
    # Fallback
    return "general"