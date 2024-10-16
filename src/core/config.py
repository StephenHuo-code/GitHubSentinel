# src/config/config.py

import os
import json

class Config:
    def __init__(self, file_path='config.json'):
        self.github_token = "your_github_token_here"
        self.notification_method = "console"
        self.openai_api_key = "your_openai_api_key_here"
        # 你可以在这里添加更多的配置参数

        self.load_from_json(file_path)
        self.load_from_env()

    def load_from_env(self):
        """从环境变量中加载配置"""
        self.github_token = os.getenv("GITHUB_API_KEY", self.github_token)
        self.notification_method = os.getenv("NOTIFICATION_METHOD", self.notification_method)
        self.openai_api_key = os.getenv("OPENAI_API_KEY", self.openai_api_key)

    def load_from_json(self, file_path):
        """从 JSON 文件中加载配置"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                config_data = json.load(f)
                self.notification_method = config_data.get("NOTIFICATION_METHOD", self.notification_method)
        except FileNotFoundError:
            print(f"配置文件 {file_path} 未找到，使用默认配置")
        except json.JSONDecodeError:
            print(f"配置文件 {file_path} 格式错误，使用默认配置")



