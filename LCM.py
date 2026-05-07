def HCF(a, b):
    if b == 0:
        return a
    return HCF(b, a % b)
def LCM(a, b):
    if a == 0 or b == 0:
        return 0
    hcf = HCF(a, b)                             # a * b = HCF(a,b) * LCM(a,b)
    return (a * b) // hcf                       # LCM(a,b) = (a * b) / HCF(a,b)
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
lcm = LCM(num1, num2)
print(f"The LCM of {num1} and {num2} is {lcm}.")