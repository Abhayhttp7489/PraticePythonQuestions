def are_strings_equal(s, t):
    if len(s) != len(t):
        return False

    for i in range(len(s)):
        if s[i] != t[i]:
            return False

    return True
print(are_strings_equal("hello", "hello"))