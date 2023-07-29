""""
star num=
end=
count no divisible by 5 and 6


"""
a = int(input("Enter start num= "))
b = int(input("Enter end num= "))
count = 0
for i in range(a, b + 1):
    if i % 5 == 0 and i % 6 == 0:
        count = count + 1
print(count)
