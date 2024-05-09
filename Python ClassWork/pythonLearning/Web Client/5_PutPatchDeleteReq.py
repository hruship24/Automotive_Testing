import requests

base_url = 'https://reqres.in'
user_id = int(input('Enter user id to update/delete'))
update_endpoint = f"/api/users/{user_id}"

update_data = {
    'Name': 'Hrushi Pawar',
    'Job': 'Senior Engineer'
}

put_response = requests.put(f"{base_url}{update_endpoint}", json=update_data)

print("PUT Response : ", put_response.status_code)
updated_user_data = put_response.json()
print("Updated User Data : ", updated_user_data)


patch_response = requests.patch(f"{base_url}{update_endpoint}", json=update_data)
print("PATCH Response : ", patch_response.status_code)
updated_user_data = patch_response.json()
print("Updated User Data : ", updated_user_data)

delete_endpoint = f"/api/users/{user_id}"

delete_response = requests.delete(f"{base_url}{delete_endpoint}")
print("DELETE Response: ", delete_response.status_code)