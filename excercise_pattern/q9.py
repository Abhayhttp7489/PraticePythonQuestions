def generate_right_angled_triangle(n):
    """
    Function to return a right-angled triangle of '*' of side n as a list of strings.

    Parameters:
    n (int): The height of the triangle.

    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    # Your code here
    triangle = []
    for i in range(1, n + 1):
        spaces = ' ' * (n - i)
        stars = '*' * i
        triangle.append(spaces + stars)
    return triangle
print(generate_right_angled_triangle(5))



