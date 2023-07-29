# ask start and end num from users and print
# all nos bet start and end divi by 5 or 7

start = int(input("Enter start num = "))
end = int(input("Enter end num = "))
i = start
while i <= end:
    if i % 5 == 0 or i % 7 == 0:
        print(i, end=" ")
    i = i + 1
