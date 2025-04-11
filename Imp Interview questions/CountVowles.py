def count_vowles(s):
    vowles = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowles:
            count += 1
    return count
print(count_vowles("Ashutosh Accenture pune"))
print(count_vowles("Ashutosh Accenture infosys pune"))