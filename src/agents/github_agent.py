import requests
import os
from datetime import datetime



class GitHubAgent:
    def __init__(self, token):
        self.base_url = "https://api.github.com"
        self.headers = {"Authorization": f"token {token}"}

    def get_repo_updates(self, repo_name, since=None, until=None):
        url = f"{self.base_url}/repos/{repo_name}/events"
        params = {}
        if since:
            params['since'] = since
        if until:
            params['until'] = until
        response = requests.get(url, headers=self.headers, params=params)
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

    def get_issues(self, repo_name, since=None, until=None):
        url = f"{self.base_url}/repos/{repo_name}/issues"
        params = {}
        if since:
            params['since'] = since
        if until:
            params['until'] = until
        response = requests.get(url, headers=self.headers, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def get_pull_requests(self, repo_name, since=None, until=None):
        url = f"{self.base_url}/repos/{repo_name}/pulls"
        params = {}
        if since:
            params['since'] = since
        if until:
            params['until'] = until
        response = requests.get(url, headers=self.headers, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
