unit = int(input("Enter units consumed = "))
if unit <= 50:
    bill = unit * 0.5
elif 50 < unit <= 150:
    bill = 25 + ((unit - 50) * 0.75)
elif 150 < unit <= 250:
    bill = 100 + ((unit - 150) * 1.2)
elif unit > 250:
    bill = 220 + ((unit - 250) * 1.5)
surcharge = bill * 0.2
total_bill = bill + surcharge
print(f"units consumed= {unit}")
print(f"bill={bill}")
print(f"surcharge={surcharge}")
print(f"total bill={total_bill}")
