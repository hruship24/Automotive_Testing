import re


def check_password_strength(password):
    # Regular expression patterns for password strength criteria
    length_pattern = r'.{8,}'
    uppercase_lowercase_pattern = r'[A-Za-z]'
    special_char_pattern = r'[@_!#$%^&*()<>?/\|}{~:]'

    # Checking if all criteria are met
    if (re.search(length_pattern, password) and
            re.search(uppercase_lowercase_pattern, password) and
            re.search(special_char_pattern, password)):
        return "Strong"
    else:
        return "Weak"


# Test the function
password = "Password@123"
print("Password strength:", check_password_strength(password))