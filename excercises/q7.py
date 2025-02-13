def generate_floyds_triangle(n):
    """
    Function to return the first n rows of Floyd's Triangle as a list of strings.

    Parameters:
    n (int): The number of rows in the triangle.

    Returns:
    list: A list of strings where each string represents a row of Floyd's Triangle.
    """
    # Your code here
    current_num = 1
    result = []
    for i in range(1, n + 1):
        row_numbers = list(range(current_num, current_num + i))
        row_str = ' '.join(map(str, row_numbers))
        result.append(row_str)
        current_num += i
    return result
print(generate_floyds_triangle(5))