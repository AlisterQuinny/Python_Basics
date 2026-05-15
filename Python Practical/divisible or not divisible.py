number=  int(input("Enter a number: "))
if(number%2==0):
        if(number%3==0):
            print("Number is divisible by 2 and 3")
        else:
            print("Number is divisible by 2 and not by 3")
else:
        if(number%3==0):
            print("Number is divisible by 3 and not by 2")
        else:
            print("Number is not divisible by neither 3 or 2")
