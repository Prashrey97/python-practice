def sum_of_n_natural_numbers(n):
    if n < 0:
        return "Input must be a non-negative integer."
    return n * (n + 1) // 2
n= int(input("Enter a non-negative integer: "))
result = sum_of_n_natural_numbers(n)
print(f"The sum of the first {n} natural numbers is: {result}")