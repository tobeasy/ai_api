# Multi AI client
This project is a simple client to send requests to multiple AI models via one simple UI.
Currently supported are:
* gemini-2.0-flash
* gemini-2.0-flash-lite-preview-02-05
* gemini-1.5-flash
* Deepseek

## Installation
Create an executable file using pyinstaller

``` 
pyinstaller build.spec
```
An executable file will then appear in the /dist directory

## Using
After the first start you have to save an api-key for the desired AI-model. To do this, just paste it in the api-key textfield and click 'Save api-key'.

## Technical description
A simple UI was built using Streamlit. It allows to select an AI model to have a conversation with and add and delete api-keys for it. 
The storage for the api-keys was created using SQLite, as no huge amount of data is expected for this application.
The Request_distributor receives the message of the user and distributes it then to the corresponding api of the selected AI model.


## License

[MIT](https://choosealicense.com/licenses/mit/)