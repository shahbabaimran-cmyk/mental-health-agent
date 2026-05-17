from dotenv import load_dotenv
from groq import Groq
import os

load_dotenv(os.path.join(os.path.dirname(__file__), "..", "venv", "secret.env"))

api_key=os.getenv("groq_api")

client = Groq(api_key=api_key)

SYSTEM_PROMPT = """You are a compassionate AI who can talk users through their problems , chat with them , listen to them and also act as a mental health first responder. Your role is to provide emotional support, not therapy or medical advice.

Core rules you NEVER break:
- Always validate feelings before offering anything else
- Never minimize, dismiss, or compare someone's pain
- Never say "I understand exactly how you feel"
- Never give medical diagnoses or prescribe anything
- Never promise that things will definitely get better
- Always remind the user they are not alone
- If someone is in crisis, prioritize connection over information
- Keep responses concise — 3 to 5 sentences max unless providing resources
- Write like a caring human, not a robot or a helpline script

Your tone: warm, grounded, present, non-judgmental."""


def compose_response(
    user_message: str,
    analysis: dict,
    route: dict,
    memory_context: str,
    chat_history: list
) -> str:
    """
    Generates the final empathetic response using all context.
    Returns the full response string including any resources.
    """

    severity = analysis.get("severity", 1)
    emotions = analysis.get("emotions", [])
    instructions = route.get("instructions", "")
    resources = route.get("resources", [])
    level = route.get("level", "calm")

    # build the composer prompt
    composer_prompt = f"""
{memory_context}

Current message analysis:
- Severity: {severity}/5
- Emotions detected: {', '.join(emotions)}
- Triage level: {level}

Your instructions for this response:
{instructions}

Now write your response to the user's message: "{user_message}"

Important:
- Write ONLY the conversational reply first (3-5 sentences)
- Do not include the resources yet — those will be appended automatically
- Do not use bullet points in your reply
- Do not start with "I" — vary your sentence openings
"""

    # build messages with history for multi-turn context
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    messages.extend(chat_history)
    messages.append({"role": "user", "content": composer_prompt})

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        temperature=0.7,  # slightly creative for warmth
        max_tokens=400
    )

    agent_reply = response.choices[0].message.content.strip()

    # append resources below the reply
    if resources:
        agent_reply += "\n\n---\n"
        for resource in resources:
            agent_reply += f"\n{resource}\n"

    return agent_reply