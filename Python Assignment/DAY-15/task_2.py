"""
Task 2: Write a Python program that handles HTTP errors gracefully (e.g., 404 or 500 errors) when making API requests.
"""

import requests


def make_api_request(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors (status codes 4xx and 5xx)
        return response.json()  # Assuming response is in JSON format
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
        return None
    except requests.exceptions.RequestException as err:
        print(f"Request error occurred: {err}")
        return None


# Example usage
url = 'https://reqres.in'
end_point = '/api/users'
data = make_api_request(f"{url}{end_point}")

if data:
    print("API request successful.")
    print("Response:")
    print(data)
else:
    print("API request failed.")