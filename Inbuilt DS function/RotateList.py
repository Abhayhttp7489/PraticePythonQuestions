def rotate_list(lst, k):
    if not lst:
        return []
    # Handle cases where k is larger than the length of the list
    k = k % len(lst)  # Ensures k is within the range of the list length

    # Rotate the list using a loop
    for _ in range(k):
        # Remove the last element and insert it at the beginning
        lst.insert(0, lst.pop())

    return lst
print(rotate_list([1, 2, 3, 4, 5], 2))