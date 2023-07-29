"""
ask a no from user
print 1 to number, which are divisible by 5

"""


n = int(input("enter a num= "))
i = 1
while i <= n:
    if i % 5 == 0:
        print(i, end=" ")
    i += 1
