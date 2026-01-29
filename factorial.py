def factorial(num):
    if num == 1:
        return num
    return num*factorial(num-1)

n = int(input("Enter a number : "))
print(f"Factorial of {n} is : {factorial(n)}")