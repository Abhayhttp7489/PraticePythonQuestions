def generate_hollow_triangle(n):
    """
        Function to return a hollow right-angled triangle of '*' of side n as a list of strings.

        Parameters:
        n (int): The height of the triangle.

        Returns:
        list: A list of strings where each string represents a row of the hollow triangle.
        """
    triangle = []
    for i in range(1, n + 1):
        if i == 1 or i == n:
            triangle.append('*' * i)
        else:
            triangle.append('*' + ' ' * (i - 2) + '*')
    return triangle
print(generate_hollow_triangle(5))