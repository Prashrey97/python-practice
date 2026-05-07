def count_digits(n):
    res = 0
    while n > 0:
        n //= 10
        res += 1
    return res
n = int(input("Enter a non-negative integer: "))
if n < 0:
    print("Input must be a non-negative integer.")
else:
    print(f"The number of digits in {n} is: {count_digits(n)}")