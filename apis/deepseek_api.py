from openai import OpenAI
import properties

class deepseek_api:
    client=None
    messages=None

    def __init__(self):
        self.client = OpenAI(api_key=properties.DEEPSEEK_API_KEY, base_url="https://api.deepseek.com")
        self.messages=[
                {"role": "system", "content": "You are a helpful assistant"},
                {"role": "user", "content": ""},
            ]

    def send_request(self, text):
        self.messages[-1]["content"] = text
        response = self.client.chat.completions.create(
            model="deepseek-chat",
            messages=self.messages,
            stream=False
        )
        self.messages.append(response.choices[0].message)
        return response.choices[0].message.content