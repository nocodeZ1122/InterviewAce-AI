from collections import defaultdict


class ConversationMemory:
    def __init__(self):
        self.sessions = defaultdict(list)

    def add_user_message(self, session_id: str, message: str):
        self.sessions[session_id].append({
            "role": "user",
            "content": message
        })

    def add_ai_message(self, session_id: str, message: str):
        self.sessions[session_id].append({
            "role": "assistant",
            "content": message
        })

    def get_history(self, session_id: str):
        return self.sessions[session_id]

    def clear(self, session_id: str):
        self.sessions[session_id] = []