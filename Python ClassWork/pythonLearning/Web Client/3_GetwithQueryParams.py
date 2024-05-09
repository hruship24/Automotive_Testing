import requests

base_url = 'https://reqres.in'
endpoint = '/api/users'

myparams = {
    'page': 1,
    'per_page': 6
}

response = requests.get(f"{base_url}{endpoint}", params=myparams)

if response.status_code == 200:
    data = response.json()
    users = data.get('data', [])
    for user in users:
        print(f"UserID : {user['id']}, "
              f"Email : {user['email']}, "
              f"First Name : {user['first_name']}, "
              f"Last Name : {user['last_name']}")
else:
    print("Error: ", response.status_code)
    