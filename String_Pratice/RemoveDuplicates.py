def remove_duplicates(s):
    seen = set()  # To track characters we've already seen
    result = []   # To store the result

    for char in s:
        if char not in seen:
            seen.add(char)  # Mark the character as seen
            result.append(char)  # Add it to the result

    return ''.join(result)  # Convert the list to a string

# Example usage:
print(remove_duplicates("programming"))  # Output: "progamin"
print(remove_duplicates("Hello, World!"))  # Output: "Helo, Wrd!"