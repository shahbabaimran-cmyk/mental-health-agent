import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agent.session_mem import SessionMemory

memory = SessionMemory()

# simulate a worsening conversation
turns = [
    ("I'm feeling a bit off today.",         {"severity": 2, "emotions": ["unease"]}),
    ("Actually I've been really struggling.", {"severity": 3, "emotions": ["sadness", "overwhelm"]}),
    ("I don't see a way out of this.",        {"severity": 4, "emotions": ["hopelessness", "despair"]}),
]

print("=" * 55)
print("  SESSION MEMORY — TREND DETECTION TEST")
print("=" * 55)

for user_msg, analysis in turns:
    memory.add_turn(user_msg, analysis, agent_response="[agent reply placeholder]")

    # ← this call is what sets self.escalated
    escalate = memory.should_escalate()

    print(f"\n📨 User     : {user_msg}")
    print(f"   Severity : {analysis['severity']}/5")
    print(f"   Trend    : {memory.get_trend()}")
    print(f"   Escalate?: {'🚨 YES' if escalate else '✅ No'}")

print("\n" + "=" * 55)
print("  CONTEXT SUMMARY")
print("=" * 55)
print(memory.get_context_summary())