# 🧠 Mental Health First Responder Agent

> An AI-powered agent that triages mental health crises in real time — detecting distress levels, routing to the right resources, and tracking mood trends across a conversation.

**Built with Groq (LLaMA 3.3) + Streamlit · 100% free to run · No model training required**

---

## 📌 The Problem

Mental health crises often go unaddressed because:
- People don't know where to turn
- Therapy is expensive and inaccessible
- Crisis hotlines can feel intimidating
- Help is needed at 3am, not during business hours

This agent acts as an **always-available first line of support** — empathetic, non-judgmental, and instant. It doesn't replace therapists. It bridges the gap until professional help is reached.

---


**Live demo →** 

---

## ⚙️ How It Works

```
User message
     │
     ▼
┌─────────────────────┐
│  Distress Analyzer  │  ← Groq LLaMA 3.3 scores severity 1–5
│                     │    and detects emotion tags
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│      Router         │  ← Routes by severity level
│                     │    calm / support / coping / crisis / emergency
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│   Session Memory    │  ← Tracks mood trend across conversation
│                     │    Auto-escalates if user is getting worse
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│ Response Composer   │  ← Groq generates warm, contextual reply
│                     │    with appropriate resources attached
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│   Streamlit UI      │  ← Chat interface + live mood trend chart
└─────────────────────┘
```

---

## 🚦 5-Level Triage System

| Level | Severity | Response |
|---|---|---|
| 🟢 **Calm** | 1/5 | Friendly check-in, warm conversation |
| 🟡 **Support** | 2/5 | Empathy + breathing exercise |
| 🟠 **Coping** | 3/5 | Validation + guided coping techniques |
| 🔴 **Crisis** | 4/5 | Deep empathy + crisis hotlines |
| 🆘 **Emergency** | 5/5 | Crisis hotlines + personalised safety plan |

Auto-escalation kicks in if the user's severity score **worsens across 3 consecutive messages** — even if no single message reaches level 4 or 5.

---

## ✨ Features

- **Real-time distress analysis** — LLM-based severity scoring, no custom model training needed
- **Emotion detection** — identifies anxiety, sadness, hopelessness, panic, anger, and more
- **5-level triage routing** — each level has a distinct response strategy
- **Auto-escalation** — worsening mood trend triggers automatic escalation
- **Contextual resources** — breathing exercises matched to detected emotion, region-specific crisis hotlines, personalised safety plans
- **Live mood trend chart** — visual severity tracker in the sidebar
- **Multi-turn memory** — full conversation context passed to every response
- **Safe messaging** — ethical guidelines baked into every prompt
- **Multi-country hotlines** — Pakistan, USA, UK, and global fallback

---

## 🛠️ Tech Stack

| Layer | Tool | Why |
|---|---|---|
| LLM Inference | Groq Cloud (LLaMA 3.1 8B Instant) | Fastest free inference available |
| Agent Logic | Python (modular architecture) | Clean, testable, extensible |
| UI | Streamlit | Rapid deployment, clean chat interface |
| Memory | In-session Python state | Zero cost, sufficient for session tracking |
| Deployment | Hugging Face Spaces | Free public hosting with shareable URL |

> **Why LLM for sentiment analysis instead of a fine-tuned classifier?**
> LLaMA 3.3 outperforms traditional sentiment models on nuanced emotional language, requires zero labeled training data, and generalizes across languages and cultural contexts out of the box.

---

## 📦 Local Setup

### Prerequisites
- Python 3.9+
- A free Groq API key from [console.groq.com](https://console.groq.com)

### Installation

```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/mental-health-agent.git
cd mental-health-agent

# 2. Create virtual environment
python -m venv venv

# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment
cp .env.example .env
# Open .env and add your Groq API key
```

### Run

```bash
streamlit run app.py
```

Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 🗂️ Project Structure

```
mental-health-agent/
│
├── app.py                          # Streamlit UI — chat interface + mood chart
│
├── agent/
│   ├── __init__.py
│   ├── distress.py        # Groq LLM scores severity 1–5 + emotion tags
│
│   ├── session_mem.py           # Tracks mood trend, detects worsening, auto-escalates
│   └── response_composer.py        # Generates final empathetic reply using full context
│
├── tools/
│   ├── __init__.py
│   ├── router.py                   # Routes to calm/support/coping/crisis/emergency
│   ├── breathing_exercises.py      # Emotion-matched breathing techniques
│   ├── hotline_lookup.py           # Crisis hotlines by country (PK, US, UK, global)
│   └── safety_plan.py              # Generates personalised safety plans
│
├── tests/
│   ├── # Tests severity scoring across 5 levels
│   ├── # Tests full routing pipeline
│   ├── # Tests trend detection + auto-escalation
│   └── End-to-end conversation simulation
│
├── requirements.txt
├── .env.example                    # Template — copy to .env and add your key
├── .gitignore
└── ETHICS.md                       # Safe messaging guidelines followed
```

---

## 🧪 Running Tests

```bash
# Test distress analyzer
python tests/test_distress_analyzer.py

# Test triage router
python tests/test_triage_router.py

# Test session memory + trend detection
python tests/test_session_memory.py

# Full end-to-end pipeline
python tests/test_full_pipeline.py
```

---

## 🔮 Roadmap

- [ ] Voice input support (Whisper API)
- [ ] Multilingual support — Urdu, Arabic, Hindi
- [ ] Anonymous session analytics dashboard
- [ ] Therapist referral integration
- [ ] Mobile app version (React Native)
- [ ] Offline fallback mode

---

## ⚖️ Ethics & Safety

This project follows **safe messaging guidelines** for mental health communication. See [ETHICS.md](ETHICS.md) for full details.

Key principles:
- Never glorifies or dramatizes distress
- Always refers to professional help in crisis situations
- Validates feelings before offering any resources
- Never promises outcomes or gives medical advice
- No conversation data is stored between sessions

> **This tool is not a replacement for professional mental health care.**
> If you or someone you know is in immediate danger, please contact emergency services.

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/voice-input`)
3. Commit your changes (`git commit -m 'add voice input support'`)
4. Push to the branch (`git push origin feature/voice-input`)
5. Open a Pull Request

---

## 👨‍💻 Author

Built by Shahbaz — AI Engineer jr.
Email : "shahbabaimran@gmail.com"

---

## 📄 License

[MIT](LICENSE) — free to use, modify, and distribute.

---

*If this project helped you or someone you care about, consider giving it a ⭐ — it helps more people find it.*
