def reverse_String(s):
    return s[::-1]
print(reverse_String("Ashutosh Accenture pune"))

def reverse_String_2(s):
    reversed_str=""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str
print(reverse_String_2("Ashutosh Accenture infosys pune"))

