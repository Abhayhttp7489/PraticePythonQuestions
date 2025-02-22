def binary_to_decimal(binary_str):
    decimal_value = 0
    for digit in binary_str:
        decimal_value = decimal_value * 2 + int(digit)
    return decimal_value
print(binary_to_decimal('10101'))