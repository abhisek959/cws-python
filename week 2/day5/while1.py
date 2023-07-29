"""
ask a start num 
ask a end num
start to end ka total

"""
start = int(input("Enter num= "))
end = int(input("Enter num= "))
i = start
total = 0
while i <= end:
    total = total + i
    i = i + 1
    print(total)
