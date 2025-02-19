def is_palindromic_tuple(tup):
    # Your code goes here
    return tup == tup[::-1]
print(is_palindromic_tuple((1, 2, 2, 1)))
