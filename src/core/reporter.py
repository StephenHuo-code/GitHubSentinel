from .llm import LLM
import datetime

class Reporter:
    def __init__(self, llm, github_agent):
            self.llm = llm
            self.github_agent = github_agent

    def report(self, updates):
        # 假设 updates 是一个列表，包含更新信息
        for update in updates:
            print(f"Update: {update}")


    def generate_release_report(self, release_info):
        report = (
            f"Latest release for {release_info['name']}:\n"
            f"Version: {release_info['tag_name']}\n"
            f"Published at: {release_info['published_at']}\n"
            f"Author: {release_info['author']['login']}\n"
            f"Release Notes:\n{release_info['body']}"
        )
        return report
    

    def generate_report(self, repo_name, start_date=None, end_date=None):
        """
        导出指定仓库的进展信息并生成报告。
        该函数使用 LLM(大型语言模型)生成报告。
        如果提供了日期范围，则导出该范围内的进展信息。
        否则，导出每日进展信息。
        """
        if not repo_name:
            print("The repository name is empty.")
            return
        if start_date and end_date:
            # Fetch issues, commits, and pull requests within the date range
            issues = self.github_agent.get_issues(repo_name, start_date, end_date)
            commits = self.github_agent.get_commits(repo_name, start_date, end_date)
            pull_requests = self.github_agent.get_pull_requests(repo_name, start_date, end_date)
            filename = f"{repo_name.replace('/', '_')}_{start_date}_to_{end_date}.md"
            title = f"Progress for {repo_name} from {start_date} to {end_date}"
        elif start_date and not end_date:  # New condition added
            end_date = datetime.datetime.now().strftime("%Y-%m-%d")  # Set end_date to today
            # Fetch issues, commits, and pull requests within the date range
            issues = self.github_agent.get_issues(repo_name, start_date, end_date)
            commits = self.github_agent.get_commits(repo_name, start_date, end_date)
            pull_requests = self.github_agent.get_pull_requests(repo_name, start_date, end_date)
            filename = f"{repo_name.replace('/', '_')}_{start_date}_to_{end_date}.md"
            title = f"Progress for {repo_name} from {start_date} to {end_date}"
        else:
            # Fetch issues, pull requests, and commits
            issues = self.github_agent.get_issues(repo_name)
            pull_requests = self.github_agent.get_pull_requests(repo_name)
            commits = self.github_agent.get_commits(repo_name)  # Fetch commits
            date_str = datetime.datetime.now().strftime("%Y-%m-%d")
            filename = f"{repo_name.replace('/', '_')}_{date_str}.md"
            title = f"Daily Progress for {repo_name} on {date_str}"
        
        with open(filename, 'w') as file:
            file.write(f"# {title}\n\n")
            file.write("## Issues\n")
            for issue in issues:
                file.write(f"- {issue['title']} (#{issue['number']})\n")
            file.write("\n## Pull Requests\n")
            for pr in pull_requests:
                file.write(f"- {pr['title']} (#{pr['number']})\n")
            file.write("\n## Commits\n")  # Add section for commits
            for commit in commits:  # Write commit messages
                file.write(f"- {commit['commit']['message']} (by {commit['commit']['author']['name']})\n")
        
        # Generate the report using LLM
        with open(filename, 'r') as file:
            markdown_content = file.read()
        
        report = self.llm.generate_report(markdown_content)
        
        # Save the generated report to a new file
        report_filename = f"report_{filename}"
        with open(report_filename, 'w') as file:
            file.write(report)
        
        return report_filename
