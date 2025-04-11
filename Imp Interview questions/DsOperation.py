list = [5, 10, 30, 181, 25]
#1. Append an element to the end of the list
list.append(6)
print(list)

#2. Insert an element at a specific index
list.insert(2, 15)
print(list)

#3. Remove an element from the list
list.remove(10)
print(list)

#4. Access an element by index
print(list[2])

#5.string manipulation
string = "Hello World"
# Convert to uppercase 
string = string.upper()
print(string)

#split the string into a list of words
words = string.split()
print(words)
#join the list of words back into a string  
string = " ".join(words)
print(string)
#6. Dictionary manipulation     
dict = {'name': 'John', 'age': 30}
# Add a new key-value pair
dict['city'] = 'New York'
print(dict)
# Remove a key-value pair   
dict.pop('age')
print(dict)
# Access a value by key
print(dict['name'])
#7. Set manipulation
set = {1, 2, 3}
# Add an element to the set
set.add(4)
print(set)


