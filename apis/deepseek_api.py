from openai import OpenAI

class deepseek_api:
    client=None
    messages=None

    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")
        self.messages = []

    def send_request(self, text):
        self.messages.append({"role": "system", "content": "You are a helpful assistant"})
        self.messages.append({"role": "user", "content": text})
        response = self.client.chat.completions.create(
            model="deepseek-chat",
            messages=self.messages,
            stream=False
        )
        self.messages.append(response.choices[0].message)
        return response.choices[0].message.content