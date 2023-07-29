# i = 10
# while i <= 200:
#     print(i, end=" ")
#     i = i + 10


# i = 1
# while i <= 100000000:
#     print(i, end=" ")
#     i = i * 10

# i = 1
# while i <= 1111111111:
#     print(i, end=" ")
#     i = (i * 10) + 1
# or
# i = 1
# n = 1
# while i <= 1111111111 and n < 10:
#     print(i, end=" ")
#     i = i + 10**n
#     n = n + 1

# i = 1
# n = 2
# while i <= 28:
#     print(i, end=" ")
#     i = i + n
#     if n == 2:
#         n = 3
#     else:
#         n = 2
# or
number = 1
counter = 2
for i in range(1, 13):
    print(number, end=" ")
    number = number + counter
    if counter == 2:
        counter = 3
    else:
        counter = 2


# i = 1
# while i <= 2048:
#     print(i, end=" ")
#     i = i + i
