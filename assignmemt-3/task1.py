num = int(input("Enter a number: "))

def factorial(n):

    result = 1

    if n < 0:
        return "Factorial is undefined for negative numbers"


    for i in range(1, n + 1):
        result *= i

    return result


result = factorial(num)

print(f"The factorial of {num} is {result}")
