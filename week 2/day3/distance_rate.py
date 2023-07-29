"""
ask user for distance(km)
base price upto 5km= 100rs
5-10km 


"""

dis = int(input("Enter dis= "))
if 0 < dis <= 5:
    bill = 100

if 5 < dis <= 10:
    bill = 100 + (dis - 5) * 50

if 10 < dis <= 15:
    bill = 350 + (dis - 10) * 40

if 15 < dis <= 20:
    bill = 550 + (dis - 15) * 30

if dis > 20:
    bill = 700 + (dis - 20) * 15

else:
    print("Invalid")

print(f"Bill= {bill}")
