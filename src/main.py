# src/main.py

from agents.github_agent import GitHubAgent
from core.subscription import SubscriptionManager
from core.updater import Updater
from core.notifier import Notifier
from core.reporter import Reporter
from services.sentinel_service import GitHubSentinelService
from core.config import Config

def main():
    config = Config()
    
    # 初始化 GitHubAgent 时使用配置类中的 token
    github_agent = GitHubAgent(config.github_token)
    subscription_manager = SubscriptionManager()
    notifier = Notifier(config.notification_method)
    reporter = Reporter()
    
    updater = Updater(github_agent, subscription_manager)
    sentinel_service = GitHubSentinelService(updater, notifier, reporter, github_agent)
    
    # Example: Add a subscription and run the service
    subscription_manager.add_subscription("octocat/Hello-World")
    sentinel_service.run()
    
    # Get the latest release of LangChain repository
    sentinel_service.report_latest_release("langchain-ai/langchain")

if __name__ == "__main__":
    main()
