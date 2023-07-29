""""
20
print factors of 20
"""

a = int(input("Enter num= "))
count = 0
for i in range(1, a + 1):
    if a % i == 0:
        print(i)
        count = count + 1
print(count)
if count == 2:
    print("prime number")

else:
    print("not a prime number")
