def factorial(n):
    if n < 0:
        return "Input must be a non-negative integer."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
n = int(input("Enter a non-negative integer: "))
result = factorial(n)
print(f"The factorial of {n} is {result}.")