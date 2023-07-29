# a1.
#  num1 = int(input("Enter num1= "))
# num2 = int(input("Enter num2= "))
# sum = num1 + num2
# print(f"Addition of {num1} and {num2} is {sum}")

# a2.
# kilometer = float(input("Enter kilometer= "))
# miles = 0.62 * (kilometer)
# print(f"{kilometer}km in miles is {miles}miles")

# a3.
# num1 = float(input("Enter number 1= "))
# num2 = float(input("Enter number 2= "))
# num3 = float(input("Enter number 3= "))
# average = (num1 + num2 + num3) / 3
# print(f"Average of 3 numbers is {average}")

# a4.
# rupee = float(input("Enter amount in rupee = "))
# paisa = rupee * 100
# print(f"Value of rupee in paisa is {paisa}")

# a5.
# s = float(input("Enter side = "))
# area_sq = s**2
# print(f"Area of square ={area_sq} ")

# a6.
games_played = int(input("Enter no. of games played = "))
games_won = int(input("Enter no. of games won = "))
games_lost = int(input("Enter no. of games lost = "))
games_tied = games_played - games_won - games_lost
tied_points = games_tied * 2
total_points = (games_won * 4) + tied_points
print(f"Tied points is {tied_points} and Total points won is {total_points}")
