import argparse
from apis import gemini_api
from apis import deepseek_api

class Multi_ai_connector:
    gemini_api=None
    deepseek_api=None

    def __init__(self, ai):
        self.ai = ai

    def send_request(self, ai, text):
        match ai:
            case "deepseek":
                if(self.deepseek_api == None):
                    self.deepseek_api = deepseek_api.deepseek_api()
                return self.deepseek_api.send_request(text)
            case _: # default case gemini
                if(self.gemini_api == None):
                    self.gemini_api = gemini_api.gemini_api()
                return self.gemini_api.send_request(text)
            

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--ai', type=str, default='keine AI', help='Name of the AI')
    args = parser.parse_args()


    user_text = input("Enter the request: ")
    multi_ai_connector = Multi_ai_connector(args.ai)

    while user_text != "exit":    
        response = multi_ai_connector.send_request(args.ai, user_text)
        print(response)
        user_text = input("Enter the request: ")

