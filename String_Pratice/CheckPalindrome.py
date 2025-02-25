def remove_duplicates(s):
    # Initialize an empty string to store the result
    result = ""

    # Iterate through each character in the input string
    for char in s:
        # If the character is not already in the result, add it
        if char not in result:
            result += char

    return result


# Example usage:
input_string = "hello world"
print(remove_duplicates(input_string))  # Output: "helo wrd"