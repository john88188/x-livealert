import os

XAI_API_KEY = os.getenv("XAI_API_KEY")
X_API_KEY = os.getenv("X_API_KEY")
X_API_SECRET = os.getenv("X_API_SECRET")
X_ACCESS_TOKEN = os.getenv("X_ACCESS_TOKEN")
X_ACCESS_TOKEN_SECRET = os.getenv("X_ACCESS_TOKEN_SECRET")

KEYWORDS = ["危机", "紧急事件", "突发新闻"]
QUERY = " OR ".join(KEYWORDS)  # 用于 Live Search 的查询字符串
MAX_RESULTS = 10
CHECK_INTERVAL = 60  # 检查间隔（秒） 