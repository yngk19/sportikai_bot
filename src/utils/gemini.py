import requests

def GetPlan(prompt):
    API_KEY = "AIzaSyACDgDdRuyt9r6vSU_KxHeSzWuyUofVUZ0"

    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=" + API_KEY

    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "contents": [{
            "parts":[{
                "text": prompt
            }]
        }]
    }

    proxies = {
        "http": "socks5h://61GFv7:FMMSuH@45.145.57.201:10860",
        "https": "socks5h://61GFv7:FMMSuH@45.145.57.201:10860"
    }

    response = requests.post(url, headers=headers, json=data, proxies=proxies)
    print(response.json())
    return response