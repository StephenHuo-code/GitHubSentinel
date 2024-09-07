# GitHub Sentinel

GitHub Sentinel 是一个用于监控 GitHub 仓库更新的工具。它可以订阅仓库，定期检查更新，并通知用户最新的发布信息。

## 功能

- **订阅仓库**：添加你感兴趣的 GitHub 仓库到订阅列表。
- **定期检查更新**：自动定期检查订阅仓库的更新。
- **通知用户**：通过配置的通知方法，通知用户最新的发布信息。
- **交互式命令行工具**：提供简单易用的命令行界面，方便用户管理订阅。
- **每日进展导出**：导出订阅项目的 issues 和 pull requests 列表到 Markdown 文件。
- **生成正式报告**：调用 GPT-4 API 生成项目每日报告。

## 安装

1. 克隆仓库：
    ```sh
    git clone https://github.com/yourusername/GitHubSentinel.git
    cd GitHubSentinel
    ```

2. 安装依赖：
    ```sh
    pip install -r requirements.txt
    ```

## 配置

在运行工具之前，请确保在项目根目录下创建一个 `config.json` 文件，并添加以下内容：


```json
{
    "github_token": "your_github_token",
    "notification_method": "your_notification_method"
}
```


## 运行：

启动交互式命令行工具：
    ```sh
    python main.py
    ```

在交互式命令行中使用以下命令：
add <repo_name>: 添加一个 GitHub 仓库到订阅列表。
remove <repo_name>: 从订阅列表中移除一个 GitHub 仓库。
update: 立即从所有订阅的仓库中获取更新。
latest_release <repo_name>: 获取指定仓库的最新版本信息。
show: 显示当前订阅的仓库列表。
quit: 退出交互工具。
Scheduler 在后台运行：


