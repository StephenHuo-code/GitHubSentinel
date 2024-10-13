import openai
import os
import logging

class LLM:
    def __init__(self, api_key, log_file='daily_progress/llm.log'):
        openai.api_key = api_key

        # Set up logging
        logging.basicConfig(filename=log_file, level=logging.INFO, 
                            format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("LLM initialized")

    def generate_report(self, markdown_content, dryrun=False):

        if dryrun:
            logging.info("Dry run mode: No API call will be made.")
            return "Dry run mode: No API call will be made."

        logging.info("Generating report for provided markdown content.")

        prompt = f"以下是项目的最新进展，根据功能合并同类项，形成一份简报，至少包含：1）新增功能；2）主要改进；3）修复问题；:\n\n{markdown_content}"
        

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content":  prompt}
            ]
        )
        report = response.choices[0].message['content']
        logging.info("Report generated successfully.")
        return report