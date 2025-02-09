#password strength checker

def is_Strong_password(password):
    """This function checks the strength of password entered by user and returns true or false"""
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char in "!@#$%^&*()-+" for char in password):
        return False
    return True

#calling a function
print(is_Strong_password("WeakPwd"))
print(is_Strong_password("Str0ngPwd!"))


