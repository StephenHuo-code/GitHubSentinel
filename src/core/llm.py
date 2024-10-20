import logging
import os
from openai import OpenAI  # 导入OpenAI库用于访问GPT模型


class LLM:
    def __init__(self, api_key, log_file='daily_progress/llm.log'):
        # 创建一个OpenAI客户端实例
        self.client = OpenAI()
        # Set up logging
        logging.basicConfig(filename=log_file, level=logging.INFO, 
                            format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("LLM initialized")

    def generate_report(self, markdown_content, dry_run=False):
        # 构建一个用于生成报告的提示文本，要求生成的报告包含新增功能、主要改进和问题修复
        prompt = (
            "以下是项目的最新进展。请根据功能合并同类项，形成一份简报，内容至少包括：\n"
            "1) 新增功能（以 commit 为主）;\n"
            "2) 主要改进（以 PR 为主）;\n"
            "3) 修复问题（以 issue 为主）。\n"
            "请使用中文输出。\n\n"
            f"{markdown_content}"
        )
        
        if dry_run:
            # 如果启用了dry_run模式，将不会调用模型，而是将提示信息保存到文件中
            logging.info("Dry run mode enabled. Saving prompt to file.")
            with open("daily_progress/prompt.txt", "w+") as f:
                f.write(prompt)
            logging.debug("Prompt saved to daily_progress/prompt.txt")
            return "DRY RUN"

        # 日志记录开始生成报告
        logging.info("Starting report generation using GPT model.")
        
        try:
            # 调用OpenAI GPT模型生成报告
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",  # 指定使用的模型版本
                messages=[
                    {"role": "user", "content": prompt}  # 提交用户角色的消息
                ]
            )
            logging.debug("GPT response: {}", response)
            # 返回模型生成的内容
            return response.choices[0].message.content
        except Exception as e:
            # 如果在请求过程中出现异常，记录错误并抛出
            logging.error("An error occurred while generating the report: {}", e)
            raise
