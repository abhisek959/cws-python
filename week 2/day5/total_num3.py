"""
ask start num 
ask end num
enter any num
print all num bet start and end divisible by any num
"""
start = int(input("Enter start num= "))
end = int(input("Enter end num= "))
any = int(input("Enter any num= "))
i = start
while i <= end:
    if i % any == 0:
        print(i)
    i = i + 1
