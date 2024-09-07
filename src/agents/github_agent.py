import requests
import os
from datetime import datetime


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

    def get_latest_release(self, repo_name):
        url = f"{self.base_url}/repos/{repo_name}/releases/latest"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def get_issues(self, repo_name):
        url = f"{self.base_url}/repos/{repo_name}/issues"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def get_pull_requests(self, repo_name):
        url = f"{self.base_url}/repos/{repo_name}/pulls"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def export_daily_progress(self, repo_name):
        if not repo_name:
            raise ValueError("Repository name cannot be empty")  # 添加检查
        issues = self.get_issues(repo_name)
        pull_requests = self.get_pull_requests(repo_name)
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
        return filename

