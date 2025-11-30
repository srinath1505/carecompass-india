# main_voice.py
from features.voice_interface import listen_for_voice, speak_text
from agents.coordinator import Coordinator
from memory import memory

def run_voice_demo():
    print("🩺 CARECOMPASS INDIA - Voice Health Concierge")
    print("Speak your health concern in Hindi, Tamil, or English.\n")

    # Get voice input
    user_voice = listen_for_voice()
    if not user_voice.strip():
        print("\n⚠️ Using fallback text query for demo...")
        user_voice = "Mujhe Chennai mein diabetes ki dawa chahiye."

    # Process with multi-agent system
    print(f"\n🧠 Processing your request for: \"{user_voice}\"")
    response = Coordinator.process_query(user_voice)

    # Speak response
    lang = memory.get("user_language", "hindi")
    print(f"\n💬 Final Response:\n{response}\n")
    
    try:
        speak_text(response, lang=lang)
        print("✅ Voice response completed.")
    except KeyboardInterrupt:
        print("\n⏹️ Voice playback interrupted (that's okay!).")
    except Exception as e:
        print(f"❌ Audio error: {e}")

if __name__ == "__main__":
    try:
        run_voice_demo()
    except Exception as e:
        print(f"💥 Fatal error: {e}")
        print("Try running again — sometimes mic access needs a retry!")