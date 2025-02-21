from google import genai
import properties

class gemini_api:
    chat = None

    def __init__(self):
        client = genai.Client(api_key=properties.GEMINI_API_KEY)
        self.chat = client.chats.create(model="gemini-2.0-flash")

    def send_request(self, text):
        try:
            response = self.chat.send_message(text)
            return response.text

        except Exception as e:
            print(f"Ein Fehler ist aufgetreten: {e}")
    

