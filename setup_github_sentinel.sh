#!/bin/bash

# 创建项目目录结构
mkdir -p GitHubSentinel/{docs,src/{agents,core,models,services},tests,config}

# 创建 README.md
cat <<EOL > GitHubSentinel/README.md
# GitHub Sentinel

GitHub Sentinel is an open-source tool designed for developers and project managers. It regularly fetches and summarizes the latest updates from subscribed GitHub repositories.

## Features
- Subscription Management
- Update Retrieval
- Notification System
- Report Generation

## Setup
- Add your GitHub token in \`main.py\`
- Add repositories to subscribe in the \`SubscriptionManager\`

## Usage
Run the service:
\`\`\`bash
python src/main.py
\`\`\`
EOL

# 创建 requirements.txt
cat <<EOL > GitHubSentinel/requirements.txt
requests
EOL

# 创建 GitHubAgent 类
cat <<EOL > GitHubSentinel/src/agents/github_agent.py
import requests

class GitHubAgent:
    def __init__(self, token):
        self.base_url = "https://api.github.com"
        self.headers = {"Authorization": f"token {token}"}

    def get_repo_updates(self, repo_name):
        url = f"{self.base_url}/repos/{repo_name}/events"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
EOL

# 创建 SubscriptionManager 类
cat <<EOL > GitHubSentinel/src/core/subscription.py
class SubscriptionManager:
    def __init__(self):
        self.subscriptions = []

    def add_subscription(self, repo_name):
        if repo_name not in self.subscriptions:
            self.subscriptions.append(repo_name)

    def remove_subscription(self, repo_name):
        if repo_name in self.subscriptions:
            self.subscriptions.remove(repo_name)

    def get_subscriptions(self):
        return self.subscriptions
EOL

# 创建 Updater 类
cat <<EOL > GitHubSentinel/src/core/updater.py
class Updater:
    def __init__(self, github_agent, subscription_manager):
        self.github_agent = github_agent
        self.subscription_manager = subscription_manager

    def fetch_updates(self):
        updates = {}
        for repo in self.subscription_manager.get_subscriptions():
            updates[repo] = self.github_agent.get_repo_updates(repo)
        return updates
EOL

# 创建 Notifier 类
cat <<EOL > GitHubSentinel/src/core/notifier.py
class Notifier:
    def notify(self, message):
        # Implement notification logic here (e.g., email, Slack, etc.)
        print(f"Notification: {message}")
EOL

# 创建 Reporter 类
cat <<EOL > GitHubSentinel/src/core/reporter.py
class Reporter:
    def generate_report(self, updates):
        report = "GitHub Repository Updates:\\n"
        for repo, events in updates.items():
            report += f"\\nRepository: {repo}\\n"
            for event in events:
                report += f"- {event['type']} by {event['actor']['login']} at {event['created_at']}\\n"
        return report
EOL

# 创建 GitHubSentinelService 类
cat <<EOL > GitHubSentinel/src/services/sentinel_service.py
class GitHubSentinelService:
    def __init__(self, updater, notifier, reporter):
        self.updater = updater
        self.notifier = notifier
        self.reporter = reporter

    def run(self):
        updates = self.updater.fetch_updates()
        report = self.reporter.generate_report(updates)
        self.notifier.notify(report)
EOL

# 创建 main.py 入口文件
cat <<EOL > GitHubSentinel/src/main.py
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
EOL

echo "GitHub Sentinel project structure has been set up successfully."
