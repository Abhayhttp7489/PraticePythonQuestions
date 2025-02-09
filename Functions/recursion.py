#calculate the factorials of a number using recursion

def factorial(n):
    if n==0:    #if n is 0,return 1 (Since 0!=1)
        return 1
    else:
        return n*factorial(n-1)   #if n>0, multiply n by the factorial of(n-1)
print(factorial(5))
