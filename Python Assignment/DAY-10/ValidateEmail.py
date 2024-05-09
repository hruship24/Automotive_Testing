import re


def validate_email(email):
    pattern = r'^[a-zA-Z0-9._]{5,}@[a-zA-Z0-9.-]{3,}\.[a-zA-Z]{2,}$'

    if re.match(pattern, email):
        return True
    else:
        return False


email = "hrushi@gmail.com"
print("Is the email valid?\n", validate_email(email))
