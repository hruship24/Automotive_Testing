"""
Task 1: Use the requests library in Python to make a GET request to a public API and print the response.
"""
import requests

# Define the URL of the API endpoint
url = "https://jsonplaceholder.typicode.com/posts/1"

# Make a GET request to the API
response = requests.get(url)

# Print the response
print(response.json())