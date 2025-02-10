#Map usually takes two input parameters like (function name, iterable)
"""def square(x):
    return x * x

numbers = [1,2,3,4,5,6,7,8,9,10]
vardef = list(map(square,numbers))
print(vardef)"""

#using with lamda function
numbers = [1,2,3,4,5,6,7,8,9,10]
vardef = list(map(lambda x:x*x,numbers))
print(vardef)

#map multiple iterables
numbers1 = [1,2,3]
numbers2 = [4,5,6]

added_numbers =list(map(lambda x,y:x+y,numbers1,numbers2))
print(added_numbers)

#use a map to convert strings to integers
str_numbers = ["1","2","3","4","5","6","7","8","9","10"]
int_numbers = list(map(int,str_numbers))
print(int_numbers)

#inbuilt function with the help of map
words = ['apple','banana','cherry']
upper_words = list(map(str.upper,words))
print(upper_words)

#map use with dictionary
def get_name(person):
    return person["name"]

people = [
    {"name":"John","age":30},
    {"name":"Jane","age":29},
    {"name":"Bob","age":31}
]
peoplenames = list(map(get_name,people))
print(peoplenames)




