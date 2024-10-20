import cmd
import argparse
from datetime import datetime, timedelta

class GitHubSentinelCLI(cmd.Cmd):
    intro = '欢迎使用 GitHub Sentinel 工具。输入 help 或 ? 查看命令列表。\n'
    prompt = '(GitHub Sentinel) '  

    def __init__(self, sentinel_service, scheduler_thread):
        super().__init__()
        self.sentinel_service = sentinel_service
        self.scheduler_thread = scheduler_thread

    def do_add(self, arg):
        '添加订阅: add <repo_name>'
        if not arg.strip():
            print("请提供仓库名称，例如：add langchain-ai/langchain")
            return
    
        parser = argparse.ArgumentParser()
        parser.add_argument('repo_name', help='仓库名称，格式: owner/repo')
        args = parser.parse_args(arg.split())
        
        if '/' not in args.repo_name:
            print("无效的仓库名称。请使用格式: owner/repo")
            return
        self.sentinel_service.subscription_manager.add_subscription(args.repo_name)

    def do_remove(self, arg):
        '移除订阅: remove <repo_name>'
        if not arg.strip():  # {{ edit_1 }}
            print("请提供仓库名称，例如：remove langchain-ai/langchain")  # {{ edit_1 }}
            return  # {{ edit_1 }}
        parser = argparse.ArgumentParser()
        parser.add_argument('repo_name', help='仓库名称，格式: owner/repo')
        args = parser.parse_args(arg.split())
        
        self.sentinel_service.subscription_manager.remove_subscription(args.repo_name)

    def do_show(self, arg):
        '显示当前订阅的仓库列表: show'
        subscriptions = self.sentinel_service.subscription_manager.get_subscriptions()
        if subscriptions:
            print("当前订阅的仓库列表:")
            for repo in subscriptions:
                print(f"- {repo}")
        else:
            print("没有订阅的仓库。")

    def do_update(self, arg):
        '手动更新所有订阅: update'
        self.sentinel_service.run()
        print("更新完成")

    def do_latest_release(self, arg):
        '获取指定仓库的最新发布: latest_release <repo_name>'
        if not arg.strip():  # {{ edit_2 }}
            print("请提供仓库名称，例如：latest_release langchain-ai/langchain")  # {{ edit_2 }}
            return  # {{ edit_2 }}
        parser = argparse.ArgumentParser()
        parser.add_argument('repo_name', help='仓库名称，格式: owner/repo')
        args = parser.parse_args(arg.split())
        
        if not args.repo_name:
            print("请提供仓库名称，例如：latest_release langchain-ai/langchain")
            return
        try:
            latest_release_info = self.sentinel_service.github_agent.get_latest_release(args.repo_name)
            release_report = self.sentinel_service.reporter.generate_release_report(latest_release_info)
            print(release_report)
        except Exception as e:
            print(f"获取最新发布信息时出错: {e}")

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

    def do_export_progress(self, arg):
        '导出每日进展: export_progress <repo_name>'
        if not arg.strip():  # {{ edit_1 }}
            print("请提供仓库名称，例如：export_progress langchain-ai/langchain")  # {{ edit_1 }}
            return  # {{ edit_1 }}
        parser = argparse.ArgumentParser()
        parser.add_argument('repo_name', help='仓库名称，格式: owner/repo')
        args = parser.parse_args(arg.split())
        
        today = datetime.now()  # {{ edit_2 }}
        since = str((today - timedelta(days=1)).date())  # {{ edit_2 }}
        until = str(today.date())  # {{ edit_2 }}

        filename = self.sentinel_service.reporter.generate_report(args.repo_name, since, until)  # {{ edit_3 }}
        if filename:
            print(f"每日进展已导出到 {filename}")

    def do_generate(self, arg):
        '生成正式报告: generate <repo_name> [start_date] [end_date]'
        if not arg.strip():  # {{ edit_4 }}
            print("请提供仓库名称，例如：generate langchain-ai/langchain 2024-10-10 2024-10-20")  # {{ edit_4 }}
            return  # {{ edit_4 }}
        parser = argparse.ArgumentParser()
        parser.add_argument('repo_name', help='仓库名称')
        parser.add_argument('start_date', nargs='?', help='开始日期 (可选)')
        parser.add_argument('end_date', nargs='?', help='结束日期 (可选)')
    
    
        args = parser.parse_args(arg.split())
       
        repo_name = args.repo_name
        start_date = args.start_date
        end_date = args.end_date

        report_filename = self.sentinel_service.reporter.generate_report(repo_name, start_date, end_date)
        
        if report_filename:
            print(f"正式报告已生成到 {report_filename}")

    def do_generate_all_report(self, arg):
        '为所有订阅的仓库生成最新发布报告: do_generate_all_report'
        subscriptions = self.sentinel_service.subscription_manager.get_subscriptions()
        if not subscriptions:
            print("没有订阅的仓库。")
            return
        
        for repo in subscriptions:
            print(f"正在为 {repo} 生成最新发布报告...")
            try:
                self.do_export_progress(repo)
                #release_report = self.sentinel_service.reporter.generate_report(repo)
                print(f"{repo} 的最新发布报告已生成。")
            except Exception as e:
                print(f"获取 {repo} 最新发布信息时出错: {e}")
