import requests

BASE = "http://127.0.0.1:8000/"

response = requests.get(BASE + "helloworld/bob/20")
print(response.json())