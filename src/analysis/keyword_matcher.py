from config.settings import KEYWORDS

class KeywordMatcher:
    def match(self, text):
        return any(keyword.lower() in text.lower() for keyword in KEYWORDS) 