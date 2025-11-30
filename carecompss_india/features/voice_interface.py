# features/voice_interface.py
import speech_recognition as sr
import pyttsx3
from utils import detect_language

# Initialize TTS engine (offline)
tts_engine = pyttsx3.init()
tts_engine.setProperty('rate', 180)  # Speed

# Set voices (Windows supports Hindi/Tamil via installed voices)
def set_voice_for_language(lang: str):
    voices = tts_engine.getProperty('voices')
    if lang == "hindi":
        # Try to find a Hindi voice (e.g., Microsoft Hemant - if installed)
        for v in voices:
            if 'hindi' in v.name.lower() or 'hemant' in v.name.lower():
                tts_engine.setProperty('voice', v.id)
                return
    elif lang == "tamil":
        # Tamil voice (e.g., Microsoft Aarav - if available)
        for v in voices:
            if 'tamil' in v.name.lower() or 'aarav' in v.name.lower():
                tts_engine.setProperty('voice', v.id)
                return
    # Fallback to default (English)
    tts_engine.setProperty('voice', voices[0].id)

def listen_for_voice(timeout=8, phrase_time_limit=12) -> str:
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Adjusting mic for ambient noise (2 sec)...")
        recognizer.adjust_for_ambient_noise(source, duration=2)
        print("🎙️ Speak now in Tamil, Hindi, or English (12 sec max):")
    with sr.Microphone() as source:
        try:
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            text = recognizer.recognize_google(audio, language="hi-IN")  # Google handles multilingual
            print(f"✅ You said: \"{text}\"")
            return text
        except Exception as e:
            print(f"❓ Voice input failed: {e}")
            return ""

def speak_text(text: str, lang: str = "english"):
    print(f"🔊 Speaking in {lang}...")
    set_voice_for_language(lang)
    try:
        tts_engine.say(text)
        tts_engine.runAndWait()
    except Exception as e:
        print(f"🔇 TTS error (falling back to text): {e}")
        print(f"\n🔊 VOICE RESPONSE:\n{text}\n")