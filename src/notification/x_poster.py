import tweepy
from config.settings import X_API_KEY, X_API_SECRET, X_ACCESS_TOKEN, X_ACCESS_TOKEN_SECRET
import logging

class XPoster:
    def __init__(self):
        self.client = tweepy.Client(
            consumer_key=X_API_KEY,
            consumer_secret=X_API_SECRET,
            access_token=X_ACCESS_TOKEN,
            access_token_secret=X_ACCESS_TOKEN_SECRET
        )
        self.logger = logging.getLogger(__name__)

    def post(self, text):
        try:
            self.client.create_tweet(text=f"⚠️ 预警: {text[:200]}...")
            return True
        except Exception as e:
            self.logger.error(f"发帖失败: {e}")
            return False 