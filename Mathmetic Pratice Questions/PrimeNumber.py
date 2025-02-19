def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):  # Check divisibility up to sqrt(n)
        if n % i == 0:
            return False
    return True

# Example test cases
print(is_prime(1))  # True
print(is_prime(4))  # False
