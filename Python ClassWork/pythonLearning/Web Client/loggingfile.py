import requests
import logging

# Configure logging
logging.basicConfig(level=logging.INFO,
                  format='%(asctime)s - %(levelname)s - %(message)s')

logging.basicConfig(filename='api_integration.log',
                    level=logging.INFO,
                    format='%(ascti+me)s - %(levelname)s - %(message)s')

# Create a session object
session = requests.Session()

# Define base URL and authentication URL
base_url = "https://restful-booker.herokuapp.com"
auth_url = f"{base_url}/auth"

# Credentials for authentication
credentials = {
    "username": "admin",
    "password": "password123"
}

# Perform authentication and log the response
response = session.post(auth_url, json=credentials)
if response.status_code == 200:
    logging.info("Authentication successful!")
    # Extract token from response JSON
    token = response.json().get('token')
    if token:
        logging.info("Token extracted from response: %s", token)
        # Manually set token as a cookie in the session
        session.cookies.set('token', token)
    else:
        logging.warning("Token not found in response JSON")
else:
    logging.error("Authentication failed: %s", response.status_code)

# Retrieve all booking IDs and log the response
get_allids_url = f"{base_url}/booking"
response_allids = session.get(get_allids_url)
all_booking_ids = response_allids.json()
first_booking_id = all_booking_ids[0]['bookingid']

if response_allids.status_code == 200:
    logging.info('First booking ID: %s', first_booking_id)
else:
    logging.error("Failed to retrieve booking IDs: %s", response_allids.status_code)

# Retrieve booking details by ID and log the response
booking_url = f"{base_url}/booking/{first_booking_id}"
logging.info('\nGet by ID Operation\nURL: %s', booking_url)
response = session.get(booking_url)
if response.status_code == 200:
    logging.info("Booking details for ID %s: %s", first_booking_id, response.text)
else:
    logging.error("Failed to retrieve booking details: %s", response.status_code)

# Delete a booking by ID and log the response
delete_booking_url = f"{base_url}/booking/{first_booking_id}"
logging.info('\nDELETE Operation\nURL: %s', delete_booking_url)
del_response = session.delete(delete_booking_url)
logging.info("DELETE response status code: %s", del_response.status_code)