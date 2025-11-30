# agents/reminder_agent.py
from adk import Tool
from memory import memory

@Tool
def create_care_reminder() -> str:
    """Generate condition-aware follow-up"""
    lang = memory.get("user_language", "english")
    condition = memory.get("user_condition", "general")
    
    # Condition-specific messages
    condition_msgs = {
        "tuberculosis": {
            "english": "Reminder: TB treatment takes 6+ months. Did you take your medicine today?",
            "hindi": "याद दिलाना: टीबी का इलाज 6+ महीने लेता है। क्या आपने आज दवा ली?",
            "tamil": "நினைவூட்டல்: காசநோய் சிகிச்சை 6+ மாதங்கள் ஆகும். இன்று மருந்தை எடுத்தீர்களா?"
        },
        "diabetes": {
            "english": "Reminder: Check your blood sugar this week. Need help finding test strips?",
            "hindi": "याद दिलाना: इस हफ्ते अपना ब्लड शुगर चेक करें। टेस्ट स्ट्रिप्स ढूंढने में मदद चाहिए?",
            "tamil": "நினைவூட்டல்: இந்த வாரம் உங்கள் இரத்த சர்க்கரையை சரிபார்க்கவும். டெஸ்ட் ஸ்ட்ரிப்ஸ் கண்டுபிடிக்க உதவி வேண்டுமா?"
        },
        "anemia": {
            "english": "Reminder: Take your Iron tablets daily. Feeling less tired?",
            "hindi": "याद दिलाना: अपनी आयरन की गोलियाँ रोज़ लें। कम थकान महसूस हो रही है?",
            "tamil": "நினைவூட்டல்: உங்கள் இரும்பு மாத்திரைகளை தினமும் எடுத்துக் கொள்ளுங்கள். குறைந்த சோர்வாக உணர்கிறீர்களா?"
        },
        "general": {
            "english": "Follow-up: Were you able to get your medicine? Need further help?",
            "hindi": "अनुस्मारक: क्या आपको अपनी दवा मिल गई? क्या आपको और सहायता चाहिए?",
            "tamil": "பின்தொடர்வு: உங்களுக்கு மருந்து கிடைத்ததா? மேலும் உதவி தேவையா?"
        }
    }
    
    msg = condition_msgs.get(condition, condition_msgs["general"]).get(lang, condition_msgs["general"]["english"])
    return msg