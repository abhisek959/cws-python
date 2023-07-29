"""
Enter n = 8
8
7 8
6 7 8
5 6 7 8
4 5 6 7 8
...
1 2 3 4 5 6 7 8

"""
a = int(input("enter num= "))
for i in range(a, 0, -1):
    for j in range(i, a + 1):
        print(j, end=" ")
    print()
