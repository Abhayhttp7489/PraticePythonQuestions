def sum_of_even_numbers(n):
    """
    Function to return the sum of the first n even natural numbers.

    Parameters:
    n (int): The number of even numbers to sum.

    Returns:
    int: The sum of the first n even natural numbers.
    """
    # Your code here
    '''total_sum = 0
    for i in range(1, n + 1):
        total_sum += 2 * i
    return total_sum
print(sum_of_even_numbers(5))'''
    return 2 * (n * (n + 1)) // 2
print(sum_of_even_numbers(10))



