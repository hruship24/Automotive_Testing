import requests

# Form data
base_url = 'https://reqres.in'
endpoint = '/api/users'

new_user_details = {
    'name': 'Hrushi',
    'job': 'Automotive tester'
}

response = requests.post(f"{base_url}{endpoint}", data=new_user_details)

if response.status_code == 201:
    user_data = response.json()
    print(user_data)
else:
    print("Error: ", response.status_code)


import requests

# JSON data
base_url = 'https://reqres.in'
endpoint = '/api/users'

new_user_details = {
    'name': 'Pawar',
    'job': 'Developer'
}

response = requests.post(f"{base_url}{endpoint}", json=new_user_details)

if response.status_code == 201:
    user_data = response.json()
    print(user_data)
else:
    print("Error: ", response.status_code)
    