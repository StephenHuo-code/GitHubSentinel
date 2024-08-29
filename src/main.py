from agents.github_agent import GitHubAgent
from core.subscription import SubscriptionManager
from core.updater import Updater
from core.notifier import Notifier
from core.reporter import Reporter
from services.sentinel_service import GitHubSentinelService

def main():
    token = "your_github_token_here"
    github_agent = GitHubAgent(token)
    subscription_manager = SubscriptionManager()
    notifier = Notifier()
    reporter = Reporter()
    
    updater = Updater(github_agent, subscription_manager)
    sentinel_service = GitHubSentinelService(updater, notifier, reporter)
    
    # Example: Add a subscription and run the service
    subscription_manager.add_subscription("octocat/Hello-World")
    sentinel_service.run()

if __name__ == "__main__":
    main()
