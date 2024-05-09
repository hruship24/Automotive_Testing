import requests


base_url = 'https://reqres.in'
endpoint = '/api/users'

response = requests.get(f"{base_url}{endpoint}")

if response.status_code == 200:
    res = response.json()
    print(res)

    users = res.get('data', [])
    for user in users:
        print(f"User Id: {user['id']}, " 
              f"Email: {user['email']}, "
              f"First Name: {user['first_name']}, "
              f"Last Name: {user['last_name']}, ")
else:
    print("Error: ",response.status_code)


base_url = 'http://reqres.in'
user_id = int(input('Enter userid between 1 - 12 : '))

endpoint = f'/api/users/{user_id}'
response = requests.get(f'{base_url}{endpoint}')

if response.status_code == 200:
    user_data = response.json()
    user = user_data.get('data', {})
    if user:
        print(f"UserID : {user['id']}, "
              f"Email : {user['email']}, "
              f"First Name : {user['first_name']}, "
              f"Last Name : {user['last_name']}")
else:
    print("Error Code: ", response.status_code, "User not found")
