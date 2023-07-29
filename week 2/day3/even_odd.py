"""
Ask num from user, print is it odd or even or equal to zero

"""
num = int(input("Enter your num= "))
if num % 2 == 0 and num != 0:
    print("Even")
if num % 2 != 0:
    print("Odd")
else:
    print("Equal to zero")
