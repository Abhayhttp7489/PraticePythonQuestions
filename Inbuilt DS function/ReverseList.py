def reverse_list(lst):
    # Your code goes here
    reverse_list=[]
    for _ in range(len(lst)):
        reverse_list.append(lst.pop())
    return reverse_list
print(reverse_list([1,2,3,4,5]))