"""
enter num1=
enter num2=
if num1 

"""
a = int(input("Enter num1= "))
b = int(input("Enter num2= "))
if a < b:
    for i in range(a, b + 1):
        print(i, end=" ")
else:
    for i in range(a, b - 1, -1):
        print(i, end=" ")
