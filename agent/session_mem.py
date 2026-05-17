from datetime import datetime


class SessionMemory:
    """
    Tracks the full conversation history and mood trend.
    Auto-escalates severity if user is getting progressively worse.
    """

    def __init__(self):
        self.messages = []          # full chat history
        self.severity_log = []      # list of severity scores over time
        self.emotion_log = []       # all emotions detected
        self.escalated = False      # flag if we force-escalated
        self.session_start = datetime.now()

    def add_turn(self, user_message: str, analysis: dict, agent_response: str):
        """Store one full conversation turn."""
        self.messages.append({
            "timestamp": datetime.now().isoformat(),
            "user": user_message,
            "severity": analysis.get("severity", 1),
            "emotions": analysis.get("emotions", []),
            "agent": agent_response
        })
        self.severity_log.append(analysis.get("severity", 1))
        self.emotion_log.extend(analysis.get("emotions", []))

    def get_trend(self) -> str:
        """
        Analyzes the last 3 severity scores.
        Returns: 'worsening', 'improving', 'stable'
        """
        if len(self.severity_log) < 2:
            return "stable"

        recent = self.severity_log[-3:]  # last 3 turns

        if recent[-1] > recent[0]:
            return "worsening"
        elif recent[-1] < recent[0]:
            return "improving"
        else:
            return "stable"

    def should_escalate(self) -> bool:
        """
        Force escalate if:
        - Last 3 messages are all severity 3+ AND worsening
        - Or any single message hits severity 5
        """
        if not self.severity_log:
            return False

        # immediate escalation on severity 5
        if self.severity_log[-1] >= 5:
            return True

        # escalate if worsening trend with 3+ turns
        if len(self.severity_log) >= 3:
            recent = self.severity_log[-3:]
            all_high = all(s >= 3 for s in recent)
            worsening = recent[-1] > recent[0]
            if all_high and worsening:
                self.escalated = True
                return True

        return False

    def get_context_summary(self) -> str:
        """
        Returns a short summary of session so far
        for the response composer to use.
        """
        if not self.messages:
            return "This is the start of the conversation."

        turn_count = len(self.messages)
        avg_severity = sum(self.severity_log) / len(self.severity_log)
        trend = self.get_trend()
        top_emotions = list(set(self.emotion_log))[:5]

        summary = f"""Session summary:
- Turns so far: {turn_count}
- Average severity: {avg_severity:.1f}/5
- Current trend: {trend}
- Emotions detected: {', '.join(top_emotions)}
- Force escalated: {self.escalated}"""

        return summary

    def get_chat_history(self) -> list:
        """
        Returns messages in Groq API format
        (for multi-turn conversation context).
        """
        history = []
        for turn in self.messages[-6:]:  # last 6 turns to stay within context
            history.append({"role": "user", "content": turn["user"]})
            history.append({"role": "assistant", "content": turn["agent"]})
        return history

    def reset(self):
        """Start a fresh session."""
        self.__init__()