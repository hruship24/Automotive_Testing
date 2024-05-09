import requests

try:
    base_url = 'http://reqres.in' # If we make changes in this it will show Error connecting to the server
    endpoint = '/api/users/2'  # If we make changes in it  , it will throw a HTTP error
    response = requests.get(f"{base_url}{endpoint}")  # timeout=0.005 it will throw a timeout error due to less time to fetch data
    if response.status_code == 200:
        print("Request was successful (Status Code:", response.status_code, ")")
        print("Response Content:", response.text)
    else:
        print("Error:", response.status_code)
    # HTTPError for non-2xx status codes
    response.raise_for_status()
except requests.exceptions.HTTPError as http_err:
    print("HTTP error occurred:", http_err)
except requests.exceptions.ConnectionError as conn_err:
    print("Error connecting to the server:", conn_err)
except requests.exceptions.Timeout as timeout_err:
    print("Timeout error occurred:", timeout_err)
except requests.exceptions.RequestException as req_err:
    print("An unexpected error occurred:", req_err)