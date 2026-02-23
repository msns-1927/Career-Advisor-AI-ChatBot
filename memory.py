from config import Config

class ChatMemory:

    def __init__(self, max_turns=Config.max_turns):
        self.history = []
        self.max_turns = max_turns

    def add(self, user_input, bot_response):
        self.history.append(f"User: {user_input}")
        self.history.append(f"Bot: {bot_response}")

        if len(self.history) > self.max_turns * 2:
            self.history = self.history[-self.max_turns * 2:]

    def get_history(self):
        return self.history