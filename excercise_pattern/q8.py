def generate_diamond(n):
    """
    Function to return a diamond pattern of '*' of side n as a list of strings.

    Parameters:
    n (int): The number of rows for the upper part of the diamond.

    Returns:
    list: A list of strings where each string represents a row of the diamond.
    """
    # Your code here
    upper = []
    for i in range(1, n + 1):
        spaces = ' ' * (n - i)
        stars = '*' * (2 * i - 1)
        row = spaces + stars + spaces
        upper.append(row)
    lower = upper[:-1][::-1]  # using slicing method and reverse
    return upper + lower
print(generate_diamond(5))