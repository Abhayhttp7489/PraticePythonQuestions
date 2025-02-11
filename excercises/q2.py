def generate_hollow_square(n):
    """
    Function to return a hollow square pattern of '*' of side n as a list of strings.

    Parameters:
    n (int): The size of the square.

    Returns:
    list: A list of strings where each string represents a row of the hollow square.
    """
    # Your code here
    return ['*' * n if i in (0, n - 1) or n <= 2 else '*' + ' ' * (n - 2) + '*' for i in range(n)]
print(generate_hollow_square(5))

