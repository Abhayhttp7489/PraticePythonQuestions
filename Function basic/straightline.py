def calculate_y(slope, intercept, x):
    """
    Function to calculate the value of y using the slope-intercept form of a line equation.

    Parameters:
    slope (float): The slope of the line.
    intercept (float): The y-intercept of the line.
    x (float): The x-coordinate for which y is to be calculated.

    Returns:
    float: The value of y corresponding to the given x.
    """
    # Calculate y using the formula y = m * x + b
    y = slope * x + intercept
    return y
print(calculate_y(2, 1, 5))