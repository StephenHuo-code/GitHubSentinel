
# src/core/notifier.py

class Notifier:
    def __init__(self, method="console"):
        self.method = method

    def notify(self, message):
        if self.method == "console":
            self._notify_console(message)
        # 你可以在这里添加更多通知方法（例如 email, Slack 等）

    def _notify_console(self, message):
        print(f"Notification: {message}")
