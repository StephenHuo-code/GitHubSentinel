import requests
import os
from datetime import datetime



class GitHubAgent:
    def __init__(self, token):
        self.base_url = "https://api.github.com"
        self.headers = {"Authorization": f"token {token}"}

    def get_latest_release(self, repo_name):
        url = f"{self.base_url}/repos/{repo_name}/releases/latest"
        params = {}
        response = requests.get(url, headers=self.headers, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def validate_date(self, date_str):
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return True
        except ValueError:
            print(f"Invalid date format: {date_str}. Expected format: YYYY-MM-DD")
            return False

    def get_commits(self, repo, since=None, until=None):
        url = f'https://api.github.com/repos/{repo}/commits'
        
        # Initialize params
        params = {'state': 'closed'}  # Default state
        if since and self.validate_date(since):
            params['since'] = since
        # Check and add until parameter
        if until and self.validate_date(until):
            params['until'] = until
        

        print(f"Fetching commits from {since} to {until}")
        
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()

    def get_issues(self, repo_name, since=None, until=None):
        url = f'https://api.github.com/repos/{repo_name}/issues'
        
        
        # Initialize params
        params = {'state': 'closed'}  # Default state
        if since and self.validate_date(since):
            params['since'] = since
        # Check and add until parameter
        if until and self.validate_date(until):
            params['until'] = until

        print(f"Fetching issues from {since} to {until}")
        
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()

    def get_pull_requests(self, repo_name, since=None, until=None):
        url = f"{self.base_url}/repos/{repo_name}/pulls"
        
        
        # Initialize params
        params = {'state': 'closed'}  # Default state
        if since and self.validate_date(since):
            params['since'] = since
        # Check and add until parameter
        if until and self.validate_date(until):
            params['until'] = until

        print(f"Fetching pull requests from {since} to {until}")
        
        response = requests.get(url, headers=self.headers, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
