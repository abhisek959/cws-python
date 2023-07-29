"""
        * 
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        * 

"""
for i in range(1, 6):
    for j in range(5, i, -1):
        print(" ", end=" ")
    for k in range(1, i + 1):
        print("*", end=" ")

    for l in range(1, i):
        print("*", end=" ")
    print()
for m in range(1, 5):
    for n in range(1, m + 1):
        print(" ", end=" ")
    for o in range(1, 6 - m):
        print("*", end=" ")
    for p in range(1, 5 - m):
        print("*", end=" ")
    print()
