# src/config/config.py

import os

class Config:
    def __init__(self):
        self.github_token = os.getenv("GITHUB_API_KEY", "your_github_token_here")
        self.notification_method = os.getenv("NOTIFICATION_METHOD", "console")
        # 你可以在这里添加更多的配置参数

    def load_from_env(self):
        """从环境变量中加载配置"""
        self.github_token = os.getenv("GITHUB_API_KEY", self.github_token)
        self.notification_method = os.getenv("NOTIFICATION_METHOD", self.notification_method)
