def merge_lists_to_dictionary(keys, values):
    # Boundary Condition to check for equal length of keys and values.
    # Last point in problem solving framework :)
    if (len(keys) != len(values)):  # len aur values equal hona chaiye merge karne ke liye dictionary mein
        return False
    # Create an empty dictionary to store the result
    result = {}

    # Use a loop to iterate through both lists
    for i in range(len(keys)):
        # Add each key-value pair to the dictionary
        result[keys[i]] = values[i]

    return result
print(merge_lists_to_dictionary(["a", "b", "c"], [1, 2, 3]))