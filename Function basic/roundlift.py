import math


def calculate_lift_rounds(n, capacity):
    """
    Function to calculate the number of rounds the lift needs to cover.

    Parameters:
    n (int): Total number of people.
    capacity (int): Maximum number of people the lift can carry in one round.

    Returns:
    int: The number of rounds required to transport all people to the top floor.
    """
    # Your code here
    rounds = math.ceil(n / capacity)
    return rounds
print(calculate_lift_rounds(10, 3))