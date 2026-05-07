# Optimized Euclidean algorithm for HCF calculation
def HCF(a, b):
    if b == 0:
        return a
    return HCF(b, a % b)
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
hcf = HCF(num1, num2)
print(f"The HCF of {num1} and {num2} is {hcf}.")

# Euclidean algorithm for GCD
#def GCD(a, b):
#    while a != b:
#        if a > b:
#            a -= b
#        else:
#            b -= a
#    return a