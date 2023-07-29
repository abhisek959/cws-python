"""
ask 3 marks from user out of 100
if pass in all subjects 
then only print total and %
else print fail
pass mark 33
"""
m1 = int(input("Enter Your Marks="))
m2 = int(input("Enter Your Marks="))
m3 = int(input("Enter Your Marks="))
if m1 >= 33 and m2 >= 33 and m3 >= 33:
    total = m1 + m2 + m3
    percentage = (total / 300) * 100
    print(f"Total= {total} and Percentage= {percentage:.2f}")
else:
    print("Fail")
