# Define the function to check even numbers
def even(x):
    return x % 2 == 0  # Returns True if even, else False

# List of numbers
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Using filter function
even_odd = list(filter(even, lst)) #filter takes first parameter as a function and second take as a list

print(even_odd)

#filter with a lambda function
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
greater_than_five = list(filter(lambda x: x > 5, numbers))
print(greater_than_five)

#filter with a lambda function and multiple conditions
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_and_greater_than_five = list(filter(lambda x: x > 5 and x % 2 == 0, numbers))
print(even_and_greater_than_five)

#filter to check ig the age is greater than 25 in dictionries
people=[
    {'name':'John','age':22},
    {'name':'Jane','age':30},
    {'name':'Dave','age':19}
]

def age_greater_than_25(person):
    return person['age'] > 25

greater_than = list(filter(age_greater_than_25,people))
print(greater_than)

