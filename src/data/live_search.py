from openai import OpenAI
from config.settings import XAI_API_KEY
import logging

class LiveSearch:
    def __init__(self):
        self.client = OpenAI(api_key=XAI_API_KEY, base_url="https://api.x.ai/v1")
        self.logger = logging.getLogger(__name__)

    def fetch_data(self, query, max_results):
        try:
            completion = self.client.chat.completions.create(
                model="grok-beta",
                messages=[
                    {"role": "system", "content": "你是一个实时数据搜索助手，使用 Live Search 功能搜索最新的相关信息。"},
                    {"role": "user", "content": f"搜索关键词：{query}，返回 {max_results} 条最新结果"}
                ],
                max_tokens=500
            )
            # 假设返回结果以换行分隔，处理成列表
            results = completion.choices[0].message.content.split("\n")
            return [result.strip() for result in results if result.strip()]
        except Exception as e:
            self.logger.error(f"Live Search 错误: {e}")
            return [] 