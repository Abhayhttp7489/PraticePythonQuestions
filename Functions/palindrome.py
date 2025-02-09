#check if a string is palindrome

def is_palindrome(s):
    s = s.lower().replace(" ","") #This makes sure uppercase and lowercase letters are treated the same and Remove spaces
    return s == s[::-1] #reverse of specific string
print(is_palindrome("Madam"))
print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("Naman"))

