def count_even_odd(lst):
    # Initialize counters for even and odd numbers
    even_count = 0
    odd_count = 0

    # Iterate through the list and count even and odd numbers
    for num in lst:
        if num % 2 == 0:  # Check if the number is even
            even_count += 1
        else:  # Otherwise, it's odd
            odd_count += 1

    # Return the counts as a tuple
    return (even_count, odd_count)
print(count_even_odd([1, 2, 3, 4, 5]))