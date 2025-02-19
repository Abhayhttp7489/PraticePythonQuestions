def is_subset(lst1, lst2):
    # Iterate through each element in lst1
    for element in lst1:
        found = False
        # Iterate through lst2 to check if the element exists
        for item in lst2:
            if element == item:
                found = True
                break  # Exit the inner loop once the element is found
        # If the element is not found in lst2, return False
        if not found:
            return False
    # If all elements in lst1 are found in lst2, return True
    return True

# Example usage:
lst1 = [1, 2, 3]
lst2 = [1, 2, 3, 4, 5]
print(is_subset(lst1, lst2))  # Output: True

lst1 = [1, 6]
lst2 = [1, 2, 3, 4, 5]
print(is_subset(lst1, lst2))  # Output: False