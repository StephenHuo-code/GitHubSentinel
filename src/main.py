# src/main.py
import argparse
import threading
import time
import cmd
from agents.github_agent import GitHubAgent
from core.subscription import SubscriptionManager
from core.updater import Updater
from core.notifier import Notifier
from core.reporter import Reporter
from core.llm import LLM
from services.sentinel_service import GitHubSentinelService
from core.config import Config

def scheduler(sentinel_service):
    while True:
        try:
            sentinel_service.run()
        except Exception as e:
            print(f"调度器遇到错误: {e}")
        finally:
            time.sleep(3600)  # 每小时运行一次

class GitHubSentinelCLI(cmd.Cmd):
    intro = '欢迎使用 GitHub Sentinel 工具。输入 help 或 ? 查看命令列表。\n'
    prompt = '(GitHub Sentinel) '  

    def __init__(self, sentinel_service, scheduler_thread):
        super().__init__()
        self.sentinel_service = sentinel_service
        self.scheduler_thread = scheduler_thread

    def do_add(self, repo_name):
        '添加订阅: add octocat/Hello-World'
        self.sentinel_service.subscription_manager.add_subscription(repo_name)

    def do_remove(self, repo_name):
        '移除订阅: remove octocat/Hello-World'
        self.sentinel_service.subscription_manager.remove_subscription(repo_name)

    def do_update(self, arg):
        '手动更新所有订阅: update'
        self.sentinel_service.run()
        print("更新完成")

    def do_latest_release(self, repo_name):
        '获取指定仓库的最新发布: latest_release octocat/Hello-World'
        self.sentinel_service.report_latest_release(repo_name)

    def do_show(self, arg):
        '显示当前订阅的仓库列表: show'
        subscriptions = self.sentinel_service.subscription_manager.get_subscriptions()
        if subscriptions:
            print("当前订阅的仓库列表:")
            for repo in subscriptions:
                print(f"- {repo}")
        else:
            print("没有订阅的仓库。")

    def do_check_thread(self, arg):
        '检查调度线程的状态: check_thread'
        if self.scheduler_thread.is_alive():
            print("调度线程正在运行")
        else:
            print("调度线程已停止")

    def do_exit(self, arg):
        '退出工具: exit'
        print('感谢使用 GitHub Sentinel 工具。再见！')
        return True

    def do_export_progress(self, repo_name):
        '导出每日进展: export_progress octocat/Hello-World'
        filename = self.sentinel_service.github_agent.export_daily_progress(repo_name)
        print(f"每日进展已导出到 {filename}")

    def do_generate_report(self, repo_name):
        '生成正式报告: generate_report octocat/Hello-World'
        if not repo_name:
            print("请提供仓库名称，例如：generate_report octocat/Hello-World")
            return
        print(f"Generating report for repo: {repo_name}")  # 调试打印
        filename = self.sentinel_service.github_agent.export_daily_progress(repo_name)
        report_filename = self.sentinel_service.reporter.generate_daily_report(filename)
        print(f"正式报告已生成到 {report_filename}")

def main():
    config = Config()
    
    # 初始化 GitHubAgent 时使用配置类中的 token
    github_agent = GitHubAgent(config.github_token)
    subscription_manager = SubscriptionManager()
    notifier = Notifier(config.notification_method)
    llm = LLM(config.openai_api_key)
    reporter = Reporter(llm)
    
    updater = Updater(github_agent, subscription_manager)
    sentinel_service = GitHubSentinelService(updater, notifier, reporter, github_agent, subscription_manager)
    
    # 启动 Scheduler 线程
    scheduler_thread = threading.Thread(target=scheduler, args=(sentinel_service,))
    scheduler_thread.daemon = True
    scheduler_thread.start()
    
    # 启动交互式命令行界面
    cli = GitHubSentinelCLI(sentinel_service, scheduler_thread)
    cli.cmdloop()

if __name__ == "__main__":
    main()

