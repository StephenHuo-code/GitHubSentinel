


class Reporter:
    def report(self, updates):
        # 假设 updates 是一个列表，包含更新信息
        for update in updates:
            print(f"Update: {update}")

    def report_release(self, release_info):
        report = (
            f"Latest release for {release_info['name']}:\n"
            f"Version: {release_info['tag_name']}\n"
            f"Published at: {release_info['published_at']}\n"
            f"Author: {release_info['author']['login']}\n"
            f"Release Notes:\n{release_info['body']}"
        )
        print(report)


'''
class Reporter:
    def generate_report(self, updates):
        report = "GitHub Repository Updates:\n"
        for repo, events in updates.items():
            report += f"\nRepository: {repo}\n"
            for event in events:
                report += f"- {event['type']} by {event['actor']['login']} at {event['created_at']}\n"
        return report

'''# services/sentinel_service.py

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
            self.reporter.report(updates)
        except Exception as e:
            print(f"Error in run method: {e}")

    def report_latest_release(self, repo_name):
        try:
            release_info = self.github_agent.get_latest_release(repo_name)
            self.reporter.report_release(release_info)
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