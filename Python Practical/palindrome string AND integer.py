print("37 Alister Quinny")
def palindrome(s):
    return s==s[::-1]
word = input("Enter a word:")
number = input("Enter a number sequence:")

if palindrome(word):
    print( word, "is a palindrome")
else:
    print( word,"is not a palindrome")
if palindrome (number):
    print(number,"is a palindrome")
else:
    print(number,"is not a palindrom")
