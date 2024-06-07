import requests

url = "https://jsonplaceholder.typicode.com/posts"

params = {
    "userId": 1
}

response = requests.get(url, params=params)

if response.status_code == 200:
    records = response.json()
    for record in records:
        print(record)
else:
    print(f"Ошибка: {response.status_code}")