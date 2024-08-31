# src/services/sentinel_service.py

class GitHubSentinelService:
    '''
    def __init__(self, updater, notifier, reporter, github_agent):
        self.updater = updater
        self.notifier = notifier
        self.reporter = reporter
        self.github_agent = github_agent
    '''


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
            self.reporter.report(updates)
        except Exception as e:
            print(f"Error in run method: {e}")

    def report_latest_release(self, repo_name):
        try:
            release_info = self.github_agent.get_latest_release(repo_name)
            report = self._generate_release_report(release_info)
            self.notifier.notify(report)
        except Exception as e:
            print(f"Error in report_latest_release method: {e}")


    def _generate_release_report(self, release_info):
        report = (
            f"Latest release for {release_info['name']}:\n"
            f"Version: {release_info['tag_name']}\n"
            f"Published at: {release_info['published_at']}\n"
            f"Author: {release_info['author']['login']}\n"
            f"Release Notes:\n{release_info['body']}"
        )
        return report


        # services/sentinel_service.py


