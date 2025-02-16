def generate_inverted_triangle(n):
    """
    Function to return an inverted right-angled triangle of '*' of side n as a list of strings.

    Parameters:
    n (int): The height and base of the triangle.

    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    if n <= 0:
        return []  # Return an empty list for invalid input

    triangle = []  # Initialize an empty list to store rows

    for i in range(n, 0, -1):  # Loop from n to 1 (decreasing order)
        triangle.append('*' * i)  # Each row contains `i` asterisks

    return triangle

# Example usage:
print("\n".join(generate_inverted_triangle(5)))
