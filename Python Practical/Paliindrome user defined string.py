def palindrome(s):
    
    return s == s[::-1]
Input =input("Enter a string:")
if palindrome(Input):
    print("is a palindrome")
else:
    print("is not a palindrome")
