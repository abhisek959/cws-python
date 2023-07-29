"""
Ask a start number = 
Ask a end number = 

Print all prime numbers between them.


"""
a = int(input("Enter start num= "))
b = int(input("Enter end num= "))

for i in range(a, b + 1):
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count = count + 1

    if count == 2:
        print(i, end=" ")


# a = int(input("Enter num= "))
# count = 0
# for i in range(1, a + 1):
#     if a % i == 0:
#         count = count + 1
# print(count)
# if count == 2:
#     print("Prime")
# else:
#     print("not prime")
