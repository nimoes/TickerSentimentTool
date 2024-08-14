from config import CLAUDE_API_KEY
from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT

class SentimentAnalyzer:
    def __init__(self):
        self.anthropic = Anthropic(api_key=CLAUDE_APY_KEY)
