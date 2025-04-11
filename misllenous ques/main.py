#1. Write a simple Python program to print an output
print("hello vs code")

#2. Write a Python code to check if a number is even or odd
def is_even(num):
    return num%2==0
print(is_even(4))
print(is_even(5))

#3. write a python code to concate two strings-
a = "vs"
b = "cursorAi"
c= a + " " + b
print(c)

#4. write a python program to find the maxium of three numbers
def max_of_three(a,b,c):
    return max(a,b,c)
print(max_of_three(10,4000,7500))

#5. write a python program to count the number of vowles in a string-
def count_vowels(s):
    return sum(1 for char in s if char.lower() in 'aeiou')
print(count_vowels("icecream vanilla"))

#6. write a python program to calculate the factorial of a number-
def factorial(n):
    if n==0:
        return 1
    return n* factorial(n-1)
print(factorial(5))

#7. write a python code to convert a string to an integer-
str="123456"
num=int(str)
print(num)

#8. write a python program to calculate the area of rectangle
def area_of_rectangle(length, width):
    return length * width
print(area_of_rectangle(9,8))

#9. write a python code to merge two dictionaries
dict1 = {'a':1, 'b':2}
dict2 = {'b':3, 'c':4}
merged = {**dict1, **dict2}
print(merged)

#10.write a python program to find common elements in two list 
list1 = [1,2,3,4,5]
list2 = [3,4,5,6]
common = list(set(list1) & (set(list2)))
print(common)

#11. write a python code to remove duplicates from a list
list1 = [1,2,2,3,3,4,4,4,5,5,6,8,8,8]
unique_list1 = list(set(list1))
print(unique_list1)

#12. write a python code to check if a string is a palindrome
def is_palindrome(s):
    return s==s[::-1]
print(is_palindrome("radar"))
print(is_palindrome("hello"))

#13. write a python program to find the longest word in a sentence
def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)
print(longest_word("i am a relatabel guy please chandigarh university give me this oppourunity !!"))

#14. write a python code to find the first non-repeating character in a string-
def non_repeating(s):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0)+1
        for char in s:
            if char_count[char] == 1:
                return char
            return None
print(non_repeating("abhayaayyyy"))

#15. write a python code to count the number of uppercase letters in a string-
def count_uppercase(s):
    return sum(1 for char in s if char.isupper())
print(count_uppercase("Nxtwave"))

#16. write a python code to implement binary search algorithm
def binary_search(arr, target):
    low, high = 0, len(arr) - 1 
    while low <= high:  
        mid = (low + high) // 2 
        if arr[mid] < target:  
            low = mid + 1
        elif arr[mid] > target:  
            high = mid - 1
        else:  
            return mid
    return -1  
print(binary_search([1,2,3,4,5,6,7],4))

#17. write a python program to revrse a string - 

def reverse_string(s):
    return s[::-1]
print(list(reverse_string("harsh")))



