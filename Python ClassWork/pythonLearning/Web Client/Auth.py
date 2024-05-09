import requests


# Authentication function
def authenticate(username, password):
    global token
    auth_url = "https://restful-booker.herokuapp.com/auth"
    credentials = {
        "username": username,
        "password": password
    }
    print('\n AUTH Operation \n ',  auth_url,'\n', credentials)
    response = requests.post(auth_url, json=credentials)
    if response.status_code == 200:
        token = response.json()["token"]
        print('Generated Token: ',token)
    return token


#POST
def create_booking(token, post_booking_data):
    bookings_url = "https://restful-booker.herokuapp.com/booking"
    post_headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
       # "Authorization": f"Bearer {token}"
    }
    print('\n POST Operation \n ',  bookings_url,'\n', post_headers,'\n',post_booking_data)
    create_booking_response = requests.post(bookings_url, json=post_booking_data, headers=post_headers)
    return create_booking_response

# PUT operation function
def update_booking(token, booking_id, booking_data):
    base_url = "https://restful-booker.herokuapp.com"
    put_booking_url = f"{base_url}/booking/{booking_id}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Cookie": f"token={token}"
    }
    print('\n PUT Operation \n ',  put_booking_url,'\n', headers,'\n',booking_data)
    response = requests.put(put_booking_url, json=booking_data, headers=headers)
    return response

# PATCH operation function
def partially_update_booking(token, booking_id, patch_data):
    base_url = "https://restful-booker.herokuapp.com"
    patch_booking_url = f"{base_url}/booking/{booking_id}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Cookie": f"token = {token}"
    }
    print('\n PATCH Operation \n ',  patch_booking_url,'\n', headers, '\n', patch_data)
    response = requests.patch(patch_booking_url, json=patch_data, headers=headers)
    return response

# DELETE operation function
def delete_booking(token, booking_id):
    base_url = "https://restful-booker.herokuapp.com"
    delete_booking_url = f"{base_url}/booking/{booking_id}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Cookie": f"token={token}"
    }
    print('\n DELETE Operation \n ',  delete_booking_url,'\n', headers)
    response = requests.delete(delete_booking_url, headers=headers)
    return response





def main():
    # Authenticate
    token = authenticate("admin", "password123")
    if token:
        print("Authentication successful!")
        # POST Operation
        post_booking_data = {
            "firstname": "John",
            "lastname": "Doe",
            "totalprice": 200,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2024-06-01",
                "checkout": "2024-06-05"
            },
            "additionalneeds": "Breakfast"
        }
        post_response = create_booking(token, post_booking_data)
        # print(post_response.text)
        print("POST response:", post_response.status_code)
        response_data = post_response.json()
        booking_id = response_data["bookingid"]
        print("Booking ID:", booking_id)

        # PUT and PATCH requests
        booking_data = {
            "firstname": "Jane",
            "lastname": "Doe",
            "totalprice": 250,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2024-07-01",
                "checkout": "2024-07-05"
            },
            "additionalneeds": "Dinner"
        }
        patch_data = {"firstname": "UpdatedFirstname"}

        # PUT
        put_response = update_booking(token, booking_id, booking_data)  # Update booking with ID 1
        print("PUT response:", put_response.status_code)
        print(put_response.json())

        # PATCH
        patch_response = partially_update_booking(token, booking_id, patch_data)  # Partially update booking with ID 1
        print("PATCH response:", patch_response.status_code)

        # DELETE
        delete_response = delete_booking(token, booking_id)
        print("DELETE response:", delete_response.status_code)
    else:
        print("Authentication failed!")


if __name__ == "__main__":
    main()