def generate_safety_plan(emotions: list) -> str:
    """
    Generates a simple personalised safety plan
    based on detected emotions.
    """

    plan = """
🛡️ **Your Personal Safety Plan**

A safety plan is a set of steps you agree to follow when things get overwhelming. Keep this somewhere accessible.

**Step 1 — Warning signs to watch for:**
- Feeling hopeless or trapped
- Withdrawing from people you care about
- Increased irritability or mood swings
- Difficulty sleeping or eating

**Step 2 — Things I can do to distract myself:**
- Take a short walk outside
- Listen to music that calms me
- Write down what I'm feeling in a journal
- Watch something comforting

**Step 3 — People I can reach out to:**
- A trusted friend or family member
- A teacher, mentor, or colleague
- A religious or community leader

**Step 4 — Professionals I can contact:**
- My doctor or therapist
- A crisis hotline (see numbers above)
- Emergency services if I feel unsafe

**Step 5 — Making my environment safer:**
- Remove or limit access to anything that could harm me
- Stay in a safe, familiar place
- Ask someone to stay with me if possible

**Remember:** This feeling is temporary. You have survived hard moments before. Help is always available.
"""
    return plan.strip()