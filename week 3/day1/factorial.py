"""
factorial
enter a num=
5= 5*4*3*2*1
"""
a = int(input("enter a num= "))
f = 1
for i in range(1, a + 1):
    f = f * i
print(f)
