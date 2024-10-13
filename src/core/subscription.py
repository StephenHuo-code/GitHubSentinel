class SubscriptionManager:
    def __init__(self):
        self.subscriptions = []

    def add_subscription(self, repo_name):
        if repo_name not in self.subscriptions:
            self.subscriptions.append(repo_name)
            print(f"订阅已添加: {repo_name}")
        else:
            print(f"订阅已存在: {repo_name}")

    def remove_subscription(self, repo_name):
        if repo_name in self.subscriptions:
            self.subscriptions.remove(repo_name)
            print(f"订阅已移除: {repo_name}")
        else:
            print(f"订阅不存在: {repo_name}")

    def get_subscriptions(self):
        return self.subscriptions
