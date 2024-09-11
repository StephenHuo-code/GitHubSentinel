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
            self.reporter.report(updates)
        except Exception as e:
            print(f"Error in run method: {e}")

    def report_latest_release(self, repo_name):
        try:
            release_info = self.github_agent.get_latest_release(repo_name)
            report = self.generate_release_report(release_info)
            self.notifier.notify(report)
        except Exception as e:
            print(f"Error in report_latest_release method: {e}")

    def generate_release_report(self, release_info):
        report = (
            f"Latest release for {release_info['name']}:\n"
            f"Version: {release_info['tag_name']}\n"
            f"Published at: {release_info['published_at']}\n"
            f"Author: {release_info['author']['login']}\n"
            f"Release Notes:\n{release_info['body']}"
        )
        return report

    def export_daily_progress(self, repo_name):
        try:
            issues = self.github_agent.get_issues(repo_name)
            pull_requests = self.github_agent.get_pull_requests(repo_name)
            date_str = datetime.now().strftime("%Y-%m-%d")
            filename = f"{repo_name.replace('/', '_')}_{date_str}.md"
            with open(filename, 'w') as file:
                file.write(f"# Daily Progress for {repo_name} on {date_str}\n\n")
                file.write("## Issues\n")
                for issue in issues:
                    file.write(f"- {issue['title']} (#{issue['number']})\n")
                file.write("\n## Pull Requests\n")
                for pr in pull_requests:
                    file.write(f"- {pr['title']} (#{pr['number']})\n")
            print(f"Daily progress exported to {filename}")
            return filename
        except Exception as e:
            print(f"Error in export_daily_progress method: {e}")

    def generate_daily_report(self, repo_name):
        try:
            markdown_file = self.export_daily_progress(repo_name)
            report_filename = self.reporter.generate_daily_report(markdown_file)
            print(f"Daily report generated to {report_filename}")
            return report_filename
        except Exception as e:
            print(f"Error in generate_daily_report method: {e}")


