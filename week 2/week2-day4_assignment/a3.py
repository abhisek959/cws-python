start = int(input("Enter start num = "))
end = int(input("Enter end num = "))
i = start
total = 0
while i <= end:
    if i % 4 == 0:
        total = total + i
    i = i + 1
print(total)
