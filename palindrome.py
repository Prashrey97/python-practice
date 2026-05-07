def isPalindrome(s):
    rev=0
    temp=s
    while temp>0:
        rev=rev*10+temp%10
        temp//=10
    return rev == s
n=int(input("Enter a number: "))
if isPalindrome(n):
    print(f"{n} is a palindrome.")
else:    print(f"{n} is not a palindrome.")

#def isPalindrome(s):
    # Remove spaces and convert to lowercase
#    s = s.replace(" ", "").lower()
    # Compare the string with its reverse
#    return s == s[::-1]
#input_string = input("Enter a string: ")
#if isPalindrome(input_string):
#    print(f'"{input_string}" is a palindrome.')
#else:    print(f'"{input_string}" is not a palindrome.')