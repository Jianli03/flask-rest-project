import requests

BASE = "http://127.0.0.1:5000/"

data = [
    {"name": "Hores", "views": 100, "likes": 10},
    {"name": "Poor Dad", "views": 10000, "likes": 3200},
    {"name": "Star war", "views": 1600, "likes": 800}
]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

input()

response = requests.delete(BASE + "video/0")
print(response.status_code)

input()

response = requests.patch(BASE + "video/2", {"views":30199, "likes": 20000})
print(response.json())

input()

response = requests.delete(BASE + "video/1")
print(response.status_code)

