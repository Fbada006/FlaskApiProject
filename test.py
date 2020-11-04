import requests

BASE = "http://127.0.0.1:5000/"
data = [{"likes": 109, "views": 100, "name": "Hello 109"},
        {"likes": 78, "views": 300, "name": "Hello 300"},
        {"likes": 90, "views": 200, "name": "Hello 200"}]

# for i in range(len(data)):
#     response = requests.put(BASE + "video/" + str(i*i), data[i])
#     print(response.json())


# input()
# response = requests.get(BASE + "video/89")
# print(response.json())

response = requests.patch(BASE + "video/2", {'views': 99, 'likes': 12312038})
print(response.json())
