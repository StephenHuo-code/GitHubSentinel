import cmd

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

    def do_latest_release(self, repo_name):
        '获取指定仓库的最新发布: latest_release DjangoPeng/GitHubSentinel'
        if not repo_name:
            print("latest_release DjangoPeng/GitHubSentinel")
            return
        try:
            # 获取最新发布信息
            latest_release_info = self.sentinel_service.github_agent.get_latest_release(repo_name)
            # 生成发布报告
            release_report = self.sentinel_service.reporter.generate_release_report(latest_release_info)
            
            # 打印报告
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

    def do_export_progress(self, repo_name):
        '导出每日进展: export_progress DjangoPeng/GitHubSentinel'
        if not repo_name:
            print("请提供仓库名称，例如：export_progress DjangoPeng/GitHubSentinel")
            return
       
        filename = self.sentinel_service.reporter.export_daily_progress(repo_name)
        if filename:
            print(f"每日进展已导出到 {filename}")

    def do_generate(self, repo_name):
        '生成正式报告: generate DjangoPeng/GitHubSentinel'
        if not repo_name:
            print("请提供仓库名称，例如：generate DjangoPeng/GitHubSentinel")
            return
        print(f"Generating report for repo: {repo_name}")  # 调试打印
        report_filename = self.sentinel_service.reporter.generate_daily_report(repo_name)
        if report_filename:
            print(f"正式报告已生成到 {report_filename}")
