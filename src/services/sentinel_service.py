class GitHubSentinelService:
    def __init__(self, updater, notifier, reporter):
        self.updater = updater
        self.notifier = notifier
        self.reporter = reporter

    def run(self):
        updates = self.updater.fetch_updates()
        report = self.reporter.generate_report(updates)
        self.notifier.notify(report)
