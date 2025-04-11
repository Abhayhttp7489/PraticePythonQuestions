def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Normalize the string
    return s == s[::-1]
print(is_palindrome("madam"))  # True
print(is_palindrome("hello"))  # False
