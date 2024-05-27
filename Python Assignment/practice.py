import requests
api = "https://reqres.in/"
endpoint = "api/users"

response = requests.get(api+endpoint)

if response.status_code == 200:
    print(response.text)
else:
    print(response.status_code)

