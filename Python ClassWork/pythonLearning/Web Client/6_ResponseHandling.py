import requests

# url = 'https://www.google.com'
# response = requests.get(url)
#
# if response.status_code == 200:
#     print("Response Headers: ")
#     for header, value in response.headers.items():
#         print(f"{header}: {value}")
#
#     print("\nResponse Context (text): ")
#     print(response.text)
#
#     print("\nResponse Content (Binary): ")
#     print(response.content[:500])
#
# else:
#     print(f"Error: {response.status_code}")


url = 'https://reqres.in/api/users'
response = requests.get(url)

if response.status_code == 200:
    headers = response.text
    print("Response Headers: ", headers)
    text_content = response.text
    print("Text Content: ", text_content)
    binary_content = response.content
    print("Binary Content Length: ", len(binary_content))

    with open("image.png", 'wb') as f:
        f.write(binary_content)
    json_content = response.json()
    print("JSON Content: ", json_content)

else:
    print("Error: ", response.status_code)
