import requests

# Wikimedia Commons
response = requests.get('https://commons.wikimedia.org/w/api.php?action=query&generator=random&grnnamespace=6&grnlimit=1&prop=imageinfo&iiprop=url&format=json', stream=True)

if response.status_code == 200:
    with open('random_image.txt', 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024):  # Read 1KB at a time
            if chunk:  # Filter out keep-alive chunks
                f.write(chunk)
else:
    print('Error:', response.status_code)

# Handling cookies and sessions (using a dummy login)
# Simulate a login by setting a session cookie
login_response = requests.post('https://reqres.in/api/login',
                               data={
                                    "email": "eve.holt@reqres.in",
                                    "password": "cityslicka"
                                    })

# Check if the login was successful (status code 200)
if login_response.status_code == 200:
    # Make a request that requires authentication
    res=login_response.json()
    tok = res['token']
    restricted_content_response = requests.post('https://reqres.in/api/users/2')  #, auth=tok)

    if restricted_content_response.status_code == 200:
        print("Restricted Content:", restricted_content_response.text)
    else:
        print('Error accessing restricted content:', restricted_content_response.status_code)
else:
    print('Error during login:', login_response.status_code)


'''
response = requests.get('https://www.wikipedia.org/', stream=True)

if response.status_code == 200:
    with open('large_response.txt', 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024):  # Read 1KB at a time
            if chunk:  # Filter out keep-alive chunks
                f.write(chunk)
else:
    print('Error:', response.status_code)

# Sets a cookie
response = requests.get('https://reqres.in/api/cookie/set', cookies={'cookie_name': 'cookie_value'})

# Uses the cookie
response = requests.get('https://reqres.in/api/cookie/get', cookies={'cookie_name': 'cookie_value'})

if response.status_code == 200:
    print("Response Content:", response.text)
else:
    print('Error:', response.status_code)
'''