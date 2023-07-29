"""
Ask num from user
if num is divisible by  2 and 3 print yes
else no
if num is less than 1 print invalid 

"""

num = int(input("Enter your num= "))
if num % 2 == 0 and num % 3 == 0 and num > 1:
    print("Yes")
elif num < 1:
    print("Invalid")
else:
    print("No")
