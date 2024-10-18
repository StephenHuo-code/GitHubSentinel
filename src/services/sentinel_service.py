# src/services/sentinel_service.py

import os
from datetime import datetime

class GitHubSentinelService:
    def __init__(self, updater, notifier, reporter, github_agent, subscription_manager):
        self.updater = updater
        self.notifier = notifier
        self.reporter = reporter
        self.github_agent = github_agent
        self.subscription_manager = subscription_manager

    def run(self):
        try:
            updates = self.updater.fetch_updates()
            self.notifier.notify(updates)
            # Moved report logic to reporter
            self.reporter.report(updates)
        except Exception as e:
            print(f"Error in run method: {e}")
