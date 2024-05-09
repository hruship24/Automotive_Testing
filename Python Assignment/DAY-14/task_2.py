"""
Task 2: Write a Python script to send a POST request with JSON data and handle the JSON response.
"""
import requests
import json

# Define the URL of the API endpoint
url = "https://reqres.in/api/users"

# Define the JSON data to be sent in the POST request
data = {
    "name": "Hrushi Pawar",
    "job": "Automotive Tester"
}

# Convert the data to JSON format
json_data = json.dumps(data)

# Set the headers for the POST request
headers = {
    "Content-Type": "application/json"
}

# Make a POST request to the API
response = requests.post(url, data=json_data, headers=headers)

# Print the JSON response
print(response.json())