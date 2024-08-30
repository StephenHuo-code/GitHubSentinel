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

    def get_latest_release(self, repo_name):
        url = f"{self.base_url}/repos/{repo_name}/releases/latest"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

