# GitHub Sentinel

[中文 README](https://github.com/StephenHuo-code/GitHubSentinel/blob/main/README.md)  


GitHub Sentinel is a tool for monitoring updates to GitHub repositories. It can subscribe to repositories, check for updates regularly, and notify users of the latest release information.

## Features

- **Subscribe to Repositories**: Add GitHub repositories you are interested in to the subscription list.
  
- **Regularly Check for Updates**: Automatically check for updates to subscribed repositories at regular intervals.
  
- **Notify Users**: Notify users of the latest release information through configured notification methods.
  
- **Interactive Command Line Tool**: Provides an easy-to-use command line interface for users to manage subscriptions.
  
- **Daily Progress Export**: Export the list of issues and pull requests for subscribed projects to a Markdown file.
  
- **Generate Formal Reports**: Call the GPT-4 API to generate daily reports for the project.

## Installation

1. Clone the repository:  
   ```sh
   git clone https://github.com/yourusername/GitHubSentinel.git
   cd GitHubSentinel
   ```

2. Install dependencies:  
   ```sh
   pip install -r requirements.txt
   ```

## Configuration

Before running the tool, make sure to set the environment variables `GITHUB_API_KEY` and `NOTIFICATION_METHOD`. For example:

## How to Run

To run GitHub Sentinel, you can use one of the following methods:

- **Command Line**: Run the following command in your terminal:  
  ```sh
  python src/command_tool.py
  ```

- **Other Methods**: Choose other running methods based on your needs.
