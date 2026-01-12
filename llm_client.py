import requests
from config import OPENROUTER_URL, HEADERS, MODEL


class LLMClient:
    def __init__(self):
        self.url = OPENROUTER_URL
        self.headers = HEADERS
        self.model = MODEL

    def call(self, messages, tools=None):
        payload = {
            "model": self.model,
            "messages": messages,
        }

        if tools:
            payload["tools"] = tools
            payload["tool_choice"] = "auto"

        response = requests.post(self.url, headers=self.headers, json=payload)
        response.raise_for_status()
        return response.json()

    def get_message_content(self, response):
        if response["choices"] and "message" in response["choices"][0]:
            return response["choices"][0]["message"]["content"]
        return None
