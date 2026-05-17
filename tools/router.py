from tools.breathing_excer import get_breathing_exercise, format_exercise
from tools.hotline import get_hotlines, format_hotlines
from tools.safety import generate_safety_plan


def route(analysis: dict, country: str = "pakistan") -> dict:
    """
    Takes distress analysis and returns the appropriate
    resources and response strategy.

    Returns:
    - level: str (calm / support / coping / crisis)
    - resources: list of formatted resource strings
    - instructions: what the response composer should do
    """

    severity = analysis.get("severity", 1)
    emotions = analysis.get("emotions", [])
    primary_emotion = emotions[0] if emotions else "default"

    # ── Level 1: Calm, no distress ──────────────────────────
    if severity == 1:
        return {
            "level": "calm",
            "resources": [],
            "instructions": "The user seems calm. Have a warm, friendly conversation. You can lightly check in on how they are doing."
        }

    # ── Level 2: Mild stress ─────────────────────────────────
    elif severity == 2:
        exercise = get_breathing_exercise(primary_emotion)
        return {
            "level": "support",
            "resources": [format_exercise(exercise)],
            "instructions": "The user is mildly stressed. Acknowledge their feelings warmly. Offer the breathing exercise gently, not forcefully."
        }

    # ── Level 3: Moderate distress ───────────────────────────
    elif severity == 3:
        exercise = get_breathing_exercise(primary_emotion)
        return {
            "level": "coping",
            "resources": [format_exercise(exercise)],
            "instructions": "The user is struggling. Show genuine empathy first — validate their feelings before suggesting anything. Then offer the breathing exercise and encourage them to talk more."
        }

    # ── Level 4: Severe distress ─────────────────────────────
    elif severity == 4:
        exercise = get_breathing_exercise(primary_emotion)
        hotlines = get_hotlines(country)
        return {
            "level": "crisis",
            "resources": [
                format_exercise(exercise),
                format_hotlines(hotlines)
            ],
            "instructions": "The user is in severe distress. Lead with deep empathy and validation. Do NOT minimize their feelings. Gently introduce the hotlines as a caring suggestion, not a dismissal."
        }

    # ── Level 5: Extreme crisis ──────────────────────────────
    else:
        hotlines = get_hotlines(country)
        safety_plan = generate_safety_plan(emotions)
        return {
            "level": "emergency",
            "resources": [
                format_hotlines(hotlines),
                safety_plan
            ],
            "instructions": "The user is in extreme crisis. This is the most important response. Be deeply human, warm, and non-judgmental. Tell them their life has value. Strongly but gently urge them to call a hotline right now. Do NOT give advice — just be present and caring."
        }