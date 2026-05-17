from dotenv import load_dotenv
from groq import Groq
import os
import json

load_dotenv(os.path.join(os.path.dirname(__file__), "..", "venv", "secret.env"))

api_key=os.getenv("groq_api")

client = Groq(api_key=api_key)

def analyze_distress(user_message: str) -> dict:
    """
    Analyzes a user message and returns:
    - severity: int 1-5
    - emotions: list of detected emotions
    - summary: one-line explanation
    """

    prompt = f"""You are a mental health triage assistant. Analyze the following message and respond ONLY with a JSON object — no extra text, no markdown, no explanation.

Message: "{user_message}"

Return this exact JSON structure:
{{
  "severity": <integer 1 to 5>,
  "emotions": [<list of emotion strings>],
  "summary": "<one sentence explaining the distress level>"
}}

Severity scale:
1 = calm, no distress
2 = mild stress or worry
3 = moderate distress, struggling
4 = severe distress, crisis signals
5 = extreme crisis, mentions of self-harm or suicide

Examples:
Message: "I'm a bit tired today" → {{"severity": 1, "emotions": ["fatigue"], "summary": "User is mildly tired but not distressed."}}
Message: "I can't stop crying and I don't know why" → {{"severity": 3, "emotions": ["sadness", "confusion", "overwhelm"], "summary": "User is experiencing emotional breakdown without a clear cause."}}
Message: "I don't want to be here anymore" → {{"severity": 5, "emotions": ["hopelessness", "suicidal ideation"], "summary": "User is expressing suicidal ideation and needs immediate crisis support."}}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4,  # low temp = consistent, predictable JSON
    )

    raw = response.choices[0].message.content.strip()

    try:
        result = json.loads(raw)
    except json.JSONDecodeError:
        # fallback if model adds extra text
        result = {
            "severity": 2,
            "emotions": ["unknown"],
            "summary": "Could not parse response. Defaulting to mild distress."
        }

    return result