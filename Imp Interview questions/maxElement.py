def max_element(lst):
    if not lst:
        return None
    max_element = lst[0]
    for element in lst:
        if element > max_element:
            max_element = element
    return max_element
my_list= [5,10,30,181,25]
print(max_element(my_list)) 
print(max_element([])) 