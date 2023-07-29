n = int(input("Enter num= "))
i = 1
total = 1
while i <= n:
    total = total + 1 / 2**i
    i = i + 1
print(total, end=" ")
