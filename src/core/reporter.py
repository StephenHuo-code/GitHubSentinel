from .llm import LLM

class Reporter:
    def __init__(self, llm):
        self.llm = llm

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

    def generate_daily_report(self, markdown_file):
        with open(markdown_file, 'r') as file:
            content = file.read()
        report = self.llm.generate_report(content)
        report_filename = markdown_file.replace(".md", "_report.md")
        with open(report_filename, 'w') as file:
            file.write(report)
        return report_filename