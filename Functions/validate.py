import re

#email validation function

def validate_email(email):
    pattern = r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$'
    return re.match(pattern, email) is not None

#calling a function
print(validate_email("test@example.com"))
print(validate_email("invalid-email"))

