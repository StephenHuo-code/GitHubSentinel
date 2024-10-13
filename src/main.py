# src/main.py
import argparse
import threading
import time
import cmd
from agents.github_agent import GitHubAgent
from core.subscription import SubscriptionManager
from core.updater import Updater
from core.notifier import Notifier
from core.reporter import Reporter
from core.llm import LLM
from services.sentinel_service import GitHubSentinelService
from core.config import Config
from cli.github_sentinel_cli import GitHubSentinelCLI

def scheduler(sentinel_service):
    while True:
        try:
            sentinel_service.run()
        except Exception as e:
            print(f"调度器遇到错误: {e}")
        finally:
            time.sleep(3600)  # 每小时运行一次

def main():
    config = Config()
    
    # 初始化 GitHubAgent 时使用配置类中的 token
    github_agent = GitHubAgent(config.github_token)
    subscription_manager = SubscriptionManager()
    notifier = Notifier(config.notification_method)
    llm = LLM(config.openai_api_key)
    reporter = Reporter(llm)
    
    updater = Updater(github_agent, subscription_manager)
    sentinel_service = GitHubSentinelService(updater, notifier, reporter, github_agent, subscription_manager)
    
    # 启动 Scheduler 线程
    scheduler_thread = threading.Thread(target=scheduler, args=(sentinel_service,))
    scheduler_thread.daemon = True
    scheduler_thread.start()
    
    # 启动交互式命令行界面
    cli = GitHubSentinelCLI(sentinel_service, scheduler_thread)
    cli.cmdloop()

if __name__ == "__main__":
    main()

