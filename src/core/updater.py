class Updater:
    def __init__(self, github_agent, subscription_manager):
        self.github_agent = github_agent
        self.subscription_manager = subscription_manager

    def fetch_updates(self):
        updates = {}
        for repo in self.subscription_manager.get_subscriptions():
            updates[repo] = self.github_agent.get_repo_updates(repo)
        return updates
