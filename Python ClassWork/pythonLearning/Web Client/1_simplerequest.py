import requests

# GET request
response = requests.get('https://www.google.com')

print("Status Code: ", response.status_code)
print("URL: ", response.url)

import http.client

# Define the target host and path
host = 'www.google.com'
path = '/'

conn = http.client.HTTPSConnection(host)
conn.request('GET', path)

response = conn.getresponse()
print("http client: ", response.status)
conn.close()
