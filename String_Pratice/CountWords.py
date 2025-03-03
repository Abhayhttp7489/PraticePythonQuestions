def count_words(s):
    # Split the string into words based on spaces
    words = s.split()
    # Return the count of words
    return len(words)

# Example usage:
print(count_words("Hello, World!"))
print(count_words("Python programming is fun."))

