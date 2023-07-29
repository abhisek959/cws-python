dis = int(input("Enter dis= "))
if dis <= 5:
    bill = 100
    print(f"Bill= {bill}")
if 5 < dis <= 10:
    bill = 100 + (dis - 5) * 50
    print(f"Bill= {bill}")
if 10 < dis <= 15:
    bill = 350 + (dis - 10) * 40
    print(f"Bill= {bill}")
if 15 < dis <= 20:
    bill = 550 + (dis - 15) * 30
    print(f"Bill= {bill}")
if dis > 20:
    bill = 700 + (dis - 20) * 20
    print(f"Bill= {bill}")