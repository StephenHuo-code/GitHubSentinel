import openai
import os

class LLM:
    def __init__(self, api_key):
        openai.api_key = api_key

    def generate_report(self, markdown_content):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Please summarize the following GitHub issues and pull requests in a formal report:\n\n{markdown_content}"}
            ]
        )
        return response.choices[0].message['content']