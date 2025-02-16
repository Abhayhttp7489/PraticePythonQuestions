#check prime number
def prime(n):
    if n < 2:
        print(n, "is not prime")
        return
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print(n, "is not prime")
            return
    print(n, "is prime")

# Taking user input
num = int(input("Enter a number: "))
prime(num)
