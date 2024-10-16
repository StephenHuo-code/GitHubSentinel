# GitHub Sentinel

GitHub Sentinel 是一个用于监控 GitHub 仓库更新的工具。它可以订阅仓库，定期检查更新，并通知用户最新的发布信息。

# GitHub Sentinel

GitHub Sentinel is a tool for monitoring updates to GitHub repositories. It can subscribe to repositories, check for updates regularly, and notify users of the latest release information.

## 功能 / Features

- **订阅仓库**：添加你感兴趣的 GitHub 仓库到订阅列表。  
  **Subscribe to Repositories**: Add GitHub repositories you are interested in to the subscription list.
  
- **定期检查更新**：自动定期检查订阅仓库的更新。  
  **Regularly Check for Updates**: Automatically check for updates to subscribed repositories at regular intervals.
  
- **通知用户**：通过配置的通知方法，通知用户最新的发布信息。  
  **Notify Users**: Notify users of the latest release information through configured notification methods.
  
- **交互式命令行工具**：提供简单易用的命令行界面，方便用户管理订阅。  
  **Interactive Command Line Tool**: Provides an easy-to-use command line interface for users to manage subscriptions.
  
- **每日进展导出**：导出订阅项目的 issues 和 pull requests 列表到 Markdown 文件。  
  **Daily Progress Export**: Export the list of issues and pull requests for subscribed projects to a Markdown file.
  
- **生成正式报告**：调用 GPT-4 API 生成项目每日报告。  
  **Generate Formal Reports**: Call the GPT-4 API to generate daily reports for the project.


## 安装 / Installation

1. 克隆仓库：  
   1. Clone the repository:  
    ```sh
    git clone https://github.com/yourusername/GitHubSentinel.git
    cd GitHubSentinel
    ```

2. 安装依赖：  
   2. Install dependencies:  
    ```sh
    pip install -r requirements.txt
    ```

## 配置 / Configuration

在运行工具之前，请确保设置环境变量 `GITHUB_API_KEY` 和 `NOTIFICATION_METHOD`。例如：  
Before running the tool, make sure to set the environment variables `GITHUB_API_KEY` and `NOTIFICATION_METHOD`. For example:

## Command Line Features / 命令行功能

- **new_command**: Description of what the new command does.  
  **new_command**: 新命令的描述。

## 如何运行 / How to Run

要运行 GitHub Sentinel，您可以使用以下方法之一：

- **命令行**：在终端中运行以下命令：  
  **Command Line**: Run the following command in your terminal:  
  ```sh
  python main.py
  ```

- **其他方法**：根据您的需求选择其他运行方式。