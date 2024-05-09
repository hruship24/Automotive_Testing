import requests

session = requests.Session()
base_url = "https://restful-booker.herokuapp.com"
auth_url = f"{base_url}/auth"
credentials = {
    "username": "admin",
    "password": "password123"
}

response = session.post(auth_url, json=credentials)
if response.status_code == 200:
    print("Authentication successful!")
    # Extract token from session cookies
    token = response.json().get('token')
    if token:
        print("Token extracted from response:", token)
        # Manually set token as a cookie in the session
        session.cookies.set('token', token)
    else:
        print("Token not found in session cookies")
else:
    print("Authentication failed:", response.status_code)


get_allids_url = 'https://restful-booker.herokuapp.com/booking'
response_allids = session.get(get_allids_url)
all_booking_ids = response_allids.json()
first_booking_id = all_booking_ids[0]['bookingid']
print('first_booking_id is ', first_booking_id)


booking_url = f"{base_url}/booking/{first_booking_id}"
print('\n Get by id Operation\n')
response = session.get(booking_url)
print('Booking Details of id : ', first_booking_id, response.text)

delete_booking_url = f"{base_url}/booking/{first_booking_id}"
print("\n DELETE Operation \n", delete_booking_url)
# No need to pass headers with token here
del_response = session.delete(delete_booking_url)
print(del_response.status_code, del_response.text)


url_with_invalid_cert = ' http://www.sslshopper.com/ssl-checker.html?hostname=secure.garthbrooks.com'

# Make a request with SSL certificate verification enabled (Default Behavior)
response_with_verification = requests.get(url_with_invalid_cert)
print("Response with SSL certificate Verification : ", response_with_verification.status_code)

# Make a request with SSL certificate verification disabled
response_without_verification = requests.get(url_with_invalid_cert, verify=False)
print("Response without SSL certificate verification: ", response_without_verification.status_code)
