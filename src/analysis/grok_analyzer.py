from openai import OpenAI
from config.settings import XAI_API_KEY
import logging

class GrokAnalyzer:
    def __init__(self):
        self.client = OpenAI(api_key=XAI_API_KEY, base_url="https://api.x.ai/v1")
        self.logger = logging.getLogger(__name__)

    def analyze(self, text):
        try:
            completion = self.client.chat.completions.create(
                model="grok-beta",
                messages=[
                    {"role": "system", "content": "你是一个预警分析助手，生成简洁的预警摘要。"},
                    {"role": "user", "content": f"分析以下文本并生成预警摘要：{text}"}
                ],
                max_tokens=100
            )
            return completion.choices[0].message.content
        except Exception as e:
            self.logger.error(f"Grok 分析错误: {e}")
            return None 