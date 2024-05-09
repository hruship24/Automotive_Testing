import json

import requests

auth_url = "https://restful-booker.herokuapp.com/auth"
credentials = {
    "username": 'admin',
    "password": 'password123'
}

print('\nAuth Operation \n',auth_url, '\n', credentials)
json_data = json.dumps(credentials) # Even if we don't convert data in json, it will be fine as it is already in json
response = requests.post(auth_url, json=credentials)

if response.status_code == 200:
    # res = response.json() to use loads we dont need to load json data again bcz it is json format
    # token = res['token']
    res_json_data = json.loads(response.content)
    token = res_json_data["token"]
    # token = response.json()['token']
    print('Generated Token: ', token)