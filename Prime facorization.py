def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def primeFactors(n):
    factors = []
    for i in range(2, n + 1):
        if isPrime(i) and n % i == 0:
            factors.append(i)
    return factors
num = int(input("Enter a number: "))
factors = primeFactors(num)
print(f"The prime factors of {num} are: {factors}.")