i = 1
while i <= 100:
    if i % 2 == 0 and i % 3 == 0 and i % 8 != 0:
        print(i, end=" ")
    i = i + 1
