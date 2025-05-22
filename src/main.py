import logging
import sys
from time import sleep
from config.settings import QUERY, MAX_RESULTS, CHECK_INTERVAL, XAI_API_KEY, X_API_KEY, X_API_SECRET, X_ACCESS_TOKEN, X_ACCESS_TOKEN_SECRET
from config.logging_config import setup_logging
from src.data.live_search import LiveSearch
from src.analysis.keyword_matcher import KeywordMatcher
from src.analysis.grok_analyzer import GrokAnalyzer
from src.notification.x_poster import XPoster

REQUIRED_ENV_VARS = {
    'XAI_API_KEY': XAI_API_KEY,
    'X_API_KEY': X_API_KEY,
    'X_API_SECRET': X_API_SECRET,
    'X_ACCESS_TOKEN': X_ACCESS_TOKEN,
    'X_ACCESS_TOKEN_SECRET': X_ACCESS_TOKEN_SECRET
}

class AlertBot:
    def __init__(self):
        setup_logging()
        self.logger = logging.getLogger(__name__)
        missing = [k for k, v in REQUIRED_ENV_VARS.items() if not v]
        if missing:
            self.logger.error(f"缺少环境变量: {', '.join(missing)}，请检查配置后重试。")
            sys.exit(1)
        self.live_search = LiveSearch()
        self.keyword_matcher = KeywordMatcher()
        self.grok_analyzer = GrokAnalyzer()
        self.x_poster = XPoster()

    def run(self):
        self.logger.info("预警机器人启动...")
        while True:
            self.logger.info("正在使用 Live Search API 获取新数据...")
            posts = self.live_search.fetch_data(QUERY, MAX_RESULTS)
            for post in posts:
                if self.keyword_matcher.match(post):
                    self.logger.info(f"关键词匹配: {post[:50]}...")
                    summary = self.grok_analyzer.analyze(post)
                    if summary:
                        self.x_poster.post(summary)
                        self.logger.info(f"已发布预警: {summary}")
            sleep(CHECK_INTERVAL) 