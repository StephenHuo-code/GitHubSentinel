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
    

    def export_daily_progress(self, repo_name):
        if not repo_name:
            print("The repository name is empty.")
            return
        issues = self.github_agent.get_issues(repo_name)
        print(issues)
        pull_requests = self.github_agent.get_pull_requests(repo_name)
        date_str = datetime.datetime.now().strftime("%Y-%m-%d")
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

    def generate_daily_report(self, repo_name):
        if not repo_name:
            print("The repository name is empty.")
            return
        markdown_file = self.export_daily_progress(repo_name)
        # Assuming generate_daily_report logic is implemented here
        # This is a placeholder for the actual report generation logic
        report_filename = f"report_{markdown_file}"
        return report_filename
