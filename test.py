import requests

BASE = "http://127.0.0.1:8000/"
headers = {"accept": "application/json"}

data = [
    {"name": "Poopy!", "views": 37, "likes": 10},
    {"name": "Thrift", "views": 70000, "likes": 1024},
    {"name": "Look, It's A Bird!", "views": 65468, "likes": 897},
    {"name": "Walrus Ahead", "views": 9999999, "likes": 9999998}
]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), json=data[i])
    print(response, response.json())
input()

""" response = requests.put(BASE + "video/1", json={"name": "Poopy!", "views": 37, "likes": 10})
print(response.json())
response = requests.put(BASE + "video/1", json={"name": "Thrift", "views": 70000, "likes": 1024})
print(response.json())
response = requests.put(BASE + "video/1", json={"name": "Look, It's A Bird!", "views": 65468, "likes": 897})
print(response.json())
response = requests.put(BASE + "video/1", json={"name": "Walrus Ahead", "views": 9999999, "likes": 9999998})
print(response.json())
input() """

response = requests.delete(BASE + "video/2")
print("Delete:")
print(response, response.text)
input()

response = requests.get(BASE + "video/3")
print("Get:")
print(response, response.text)