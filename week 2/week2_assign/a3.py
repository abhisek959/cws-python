a1 = int(input("Enter angles of triangle= "))
a2 = int(input("Enter angles of triangle= "))
a3 = int(input("Enter angles of triangle= "))
if a1 + a2 + a3 == 180:
    if a1 == a2 == a3 == 60:
        print("Equilateral triangle")
    elif a1 == 90 or a2 == 90 or a3 == 90:
        print("Right angled triangle")
    elif a1 == a2 or a2 == a3 or a3 == a1:
        print("Isosceles Triangle")
    else:
        print("Scalene triangle")
else:
    print("Invalid")
