"""
5                 2
4 5               3
3 4 5             4
2 3 4 5           5
1 2 3 4 5         6


"""


for i in range(5, 0, -1):
    for j in range(i, 6):
        print(j, end=" ")
    print()
