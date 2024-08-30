# src/services/sentinel_service.py

class GitHubSentinelService:
    def __init__(self, updater, notifier, reporter, github_agent):
        self.updater = updater
        self.notifier = notifier
        self.reporter = reporter
        self.github_agent = github_agent

    def run(self):
        updates = self.updater.fetch_updates()
        report = self.reporter.generate_report(updates)
        self.notifier.notify(report)

    def report_latest_release(self, repo_name):
        release_info = self.github_agent.get_latest_release(repo_name)
        report = self._generate_release_report(release_info)
        self.notifier.notify(report)

    def _generate_release_report(self, release_info):
        report = (
            f"Latest release for {release_info['name']}:\n"
            f"Version: {release_info['tag_name']}\n"
            f"Published at: {release_info['published_at']}\n"
            f"Author: {release_info['author']['login']}\n"
            f"Release Notes:\n{release_info['body']}"
        )
        return report
