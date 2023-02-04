import requests
import json

# API endpoint do ChatGPT
API_URL = "https://api.openai.com/v1/engines/davinci/jobs"

# Chave API da sua conta OpenAI
API_KEY = "your-api-key"

def ask_chatgpt(question):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    data = {
        "prompt": question,
        "max_tokens": 256,
        "n": 1,
        "stop": "",
        "temperature": 0.5
    }

    response = requests.post(API_URL, headers=headers, data=json.dumps(data))
    response_text = response.json()["choices"][0]["text"]
    return response_text

def lambda_handler(event, context):
    # Recebendo a pergunta do usuário
    user_question = event["request"]["intent"]["slots"]["question"]["value"]

    # Enviando a pergunta para o ChatGPT
    chatgpt_answer = ask_chatgpt(user_question)

    # Preparando a resposta para o usuário
    response = {
        "version": "1.0",
        "response": {
            "outputSpeech": {
                "type": "PlainText",
                "text": chatgpt_answer
            }
        }
    }

    return response
