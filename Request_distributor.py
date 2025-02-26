from apis import gemini_api
from apis import deepseek_api

class Request_distributor:
    gemini_api=None
    deepseek_api=None

    def __init__(self):
        pass
        

    def send_request(self, ai, text, api_key):
        match ai:
            case "Deepseek":
                if(self.deepseek_api == None):
                    self.deepseek_api = deepseek_api.deepseek_api(api_key)
                return self.deepseek_api.send_request(text)
            case "Gemini-2.0-flash-lite Preview":
                if(self.gemini_api == None):
                    self.gemini_api = gemini_api.gemini_api("gemini-2.0-flash-lite-preview-02-05", api_key)
                return self.gemini_api.send_request(text)
            case "Gemini 1.5 Flash":
                if(self.gemini_api == None):
                    self.gemini_api = gemini_api.gemini_api("gemini-1.5-flash", api_key)
                return self.gemini_api.send_request(text)
            case _: # default case gemini
                if(self.gemini_api == None):
                    self.gemini_api = gemini_api.gemini_api("gemini-2.0-flash", api_key)
                return self.gemini_api.send_request(text)
    
