def generate_number_triangle(n):
    """
    Function to return a right-angled triangle of repeated numbers of side n as a list of strings.

    Parameters:
    n (int): The height of the triangle.

    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    # Initialize an empty list to store the rows of the triangle
    triangle = []

    # Loop through each row from 1 to n
    for i in range(1, n + 1):
        # Create a row with the digit i repeated i times
        row = str(i) * i
        # Add the row to the list
        triangle.append(row)

    # Return the list of rows
    return triangle
print(generate_number_triangle(5))
