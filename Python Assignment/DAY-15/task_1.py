"""
Task 1: Create a Python script that uses OAuth authentication to connect to a RESTful service.
"""
import requests

# Base URL of the Simple Books API
base_url = 'https://simple-books-api.glitch.me'


def register_api_client(client_name, client_email):
    # Endpoint for registering API client
    endpoint = f'{base_url}/api-clients/'

    # Request body
    data = {
        "clientName": client_name,
        "clientEmail": client_email
    }

    # Make POST request to register client
    response = requests.post(endpoint, json=data)

    # Check if registration was successful
    if response.status_code == 201:
        access_token = response.json().get('accessToken')
        return access_token
    else:
        print(f"Failed to register API client. Status code: {response.status_code}")
        print(f"Response: {response.text}")
        return None


def main():
    # Replace these values with your client credentials
    client_name = 'Hrushipa'
    client_email = 'abcdef@mail.com'

    # Register API client
    access_token = register_api_client(client_name, client_email)

    if access_token:
        print("API client registered successfully.")
        print("Access Token:", access_token)
        print("Now you can use this access token to authenticate requests to the Simple Books API.")
    else:
        print("Failed to obtain access token. Please check the error messages.")


if __name__ == "__main__":
    main()
