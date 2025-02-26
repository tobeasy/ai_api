from google import genai

class gemini_api:
    model = None
    chat = None

    def __init__(self, model, api_key):
        client = genai.Client(api_key=api_key)
        self.chat = client.chats.create(model=model)

    def send_request(self, text):
        try:
            response = self.chat.send_message(text)
            if response.status_code != 200:
                return f"Error contacting Gemini. Status code: {response.status_code}"
            else:
                return response.text

        except Exception as e:
            print(f"Error contacting Gemini: {e}")
    

