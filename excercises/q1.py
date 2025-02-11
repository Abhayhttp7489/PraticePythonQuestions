"""
    Function to return a square pattern of '*' of side n as a list of strings.

    Parameters:
    n (int): The size of the square.

    Returns:
    list: A list of strings where each string represents a row of the square.
    """
def square(n):
    return [n * '*' for i in range(n)]
print(square(5))
