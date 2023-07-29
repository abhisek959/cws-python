unit = int(input("Enter units consumed = "))
rate = int(input("Enter rate = "))
base_cost = unit * rate
tax = base_cost * 0.12
total_cost = base_cost + tax
if total_cost > 100 and total_cost % 5 == 0:
    print(
        f"The cost of your light bill is ${total_cost}.There is a free gift card to your favourite store."
    )
else:
    print(f"The cost of your light bill is ${total_cost}")
