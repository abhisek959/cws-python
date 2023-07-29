"""
enter a num=15

1 3 5 15
"""
num = int(input("Enter num= "))
i = 1
count = 0
while i <= num:
    if num % i == 0:
        count = count + 1
        print(i)
    i = i + 1
if count == 2:
    print("it is a prime num")
else:
    print("it is not a prime num")
