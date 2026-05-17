def get_breathing_exercise(emotion: str) -> dict:
    """
    Returns a breathing exercise based on the detected emotion.
    """

    exercises = {
        "anxiety": {
            "name": "Box Breathing",
            "steps": [
                "Inhale slowly through your nose for 4 counts",
                "Hold your breath for 4 counts",
                "Exhale slowly through your mouth for 4 counts",
                "Hold for 4 counts",
                "Repeat 4 times"
            ],
            "why": "Box breathing activates your parasympathetic nervous system, reducing anxiety fast."
        },
        "panic": {
            "name": "4-7-8 Breathing",
            "steps": [
                "Inhale through your nose for 4 counts",
                "Hold your breath for 7 counts",
                "Exhale completely through your mouth for 8 counts",
                "Repeat 3-4 times"
            ],
            "why": "The extended exhale signals your brain to calm down immediately."
        },
        "sadness": {
            "name": "Deep Belly Breathing",
            "steps": [
                "Place one hand on your chest, one on your belly",
                "Inhale deeply so your belly rises (not your chest)",
                "Hold for 2 counts",
                "Exhale slowly for 6 counts",
                "Repeat for 2 minutes"
            ],
            "why": "Deep belly breathing releases tension held in the body during grief or sadness."
        },
        "anger": {
            "name": "Cooling Breath",
            "steps": [
                "Curl your tongue and inhale through it like a straw",
                "Hold for 4 counts",
                "Exhale slowly through your nose for 6 counts",
                "Repeat 5-6 times"
            ],
            "why": "The cooling breath physically lowers body temperature and reduces anger response."
        },
        "default": {
            "name": "Simple Calming Breath",
            "steps": [
                "Inhale slowly for 4 counts",
                "Exhale slowly for 6 counts",
                "Focus only on your breath",
                "Repeat for 2 minutes"
            ],
            "why": "Slowing your breath sends a calm signal to your nervous system."
        }
    }

    # match emotion to exercise, fallback to default
    for key in exercises:
        if key in emotion.lower():
            return exercises[key]

    return exercises["default"]


def format_exercise(exercise: dict) -> str:
    lines = [f"🫁 **{exercise['name']}**\n"]
    for i, step in enumerate(exercise["steps"], 1):
        lines.append(f"  {i}. {step}")
    lines.append(f"\n💡 *{exercise['why']}*")
    return "\n".join(lines)