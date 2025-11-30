### 📄 **CareCompass India – Project Documentation**

**Title**: CareCompass India**Subtitle**: An open-source, multilingual AI health concierge that connects underserved Indian citizens to life-saving public health schemes, medicine, and hospitals — in their own language.

#### Built for the Google AI Agents Intensive Capstone (Nov 2025)

**Track**: Agents for Good**Languages Supported**: Hindi, Tamil, English

### 🌍 The Problem

India runs dozens of life-saving public health programs:

*   **Jan Aushadhi**: 50–80% cheaper generic medicines
    
*   **Ayushman Bharat**: ₹5 lakh free hospitalization
    
*   **Nikshay Poshan Yojana**: ₹500/month for TB patients
    
*   **Anemia Mukt Bharat**: Free Iron tablets for women & children
    

Yet millions remain unaware—especially the elderly, rural, and low-literacy—because:

*   Schemes are buried in English websites
    
*   Helplines are understaffed
    
*   Local ASHA workers can’t scale
    

Result: Preventable suffering, despite available help.

### 💡 Our Solution

**CareCompass India** is a voice-first, multilingual AI agent that:

*   Listens to symptoms in spoken Hindi/Tamil/English
    
*   Infers conditions (e.g., “night fever + cough” → Tuberculosis)
    
*   Responds with personalized, actionable guidance:
    
    *   Nearest Jan Aushadhi / Amma Pharmacy
        
    *   PMJAY-empaneled hospitals
        
    *   Relevant state & central schemes
        
*   Ends with real next steps:\[1\] 🏪 Amma Pharmacy, Teynampet\[2\] 📞 1800-425-1111\[3\] 💻 Book e-Sevai
    

It’s not a chatbot—it’s a digital ASHA worker.

### 🏗️ Technical Architecture

CareCompass uses a **multi-agent system** inspired by Google ADK patterns:

AgentRoleCoordinatorOrchestrates workflowSymptom MapperInfers condition from symptomsMedicine AgentFinds affordable medicine storesHospital AgentLocates PMJAY hospitalsSchemes AgentRetrieves state-specific schemesLanguage AgentFormats responses in user’s languageReminder AgentSends condition-aware follow-ups

**Key Features**:

*   Voice I/O (speech-to-text + text-to-speech, offline)
    
*   Grounded responses using real Indian public data
    
*   Zero hallucination—only resource navigation
    
*   Ethical by design—no PII stored
    

### 🚀 Quick Start

**Prerequisites**:

*   Python 3.10+
    
*   Microphone (for voice demo)
    

**Installation**:

1.  Open terminal
    
2.  Run:git clone https://github.com/srinath1505/.git
    
    cd carecompass-india
    
    python -m venv venv
    
    source venv/bin/activate # Linux/Mac
    
    venv\\Scripts\\activate # Windows
    
    pip install -r requirements.txt
    

**Run**:

*   Text demo: python main.py
    
*   Voice demo: python main\_voice.py
    

> Note: Allow microphone access on first run.

### 📂 Project Structure carecompass-india/

 ├── agents/

 ├── data/

├── features/

 ├── main.py

 ├── main\_voice.py

├── memory.py

 ├── utils.py

 ├── adk.py

 ├── requirements.txt

 └── README.md

### 📊 Data Sources (Mocked from Real Programs)

*   Medicine Stores: [https://janaushadhi.gov.in](https://janaushadhi.gov.in/)
    
*   Hospitals: [https://hospitals.pmjay.gov.in](https://hospitals.pmjay.gov.in/)
    
*   Schemes: State health dept. websites (TN, MH, KA, UP, WB, GJ)
    

> Privacy: All data is public, anonymized, and non-sensitive. No real user data is collected.

### 🎥 Demo

_(Insert your 60-second video link here)_

Shows:

*   Voice input in Tamil: “எனக்கு மூன்று வாரங்களாக இருமல் இருக்கு...”
    
*   Agent detects TB, finds Nikshay Poshan Yojana
    
*   Reads response aloud + shows quick actions
    

### 🤝 Contributing

We welcome contributions! Ways to help:

*   Add Marathi, Bengali, Telugu support
    
*   Integrate real APIs (Nikshay, ABDM, e-Sevai)
    
*   Improve symptom-condition mapping
    
*   Build WhatsApp/IVR interface
    

### ⚖️ Ethics & Limitations

*   ❌ Not a medical device—never gives diagnosis or treatment advice
    
*   ✅ Always says: “Consult a doctor”
    
*   🔒 No data collection—runs entirely locally
    
*   🌐 Built for non-smartphone, low-literacy users
    

This project is for educational and social impact purposes only.

### 📜 License

MIT License

### 🙏 Acknowledgements

*   Google AI Agents Intensive Course (Nov 2025)
    
*   Government of India: Ayushman Bharat, Jan Aushadhi, Nikshay
    
*   Public health workers & ASHA volunteers across India
    

### 📬 Contact

Built with ❤️ for Bharat.Questions? Open an issue on GitHub or email [srinathselvakumar1505@gmail.com](mailto:srinathselvakumar1505@gmail.com).

> “Technology is best when it brings people together.” — Matt Mullenweg
