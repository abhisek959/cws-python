"""

logical operators(result always in boolean)
AND, OR, NOT

"""
physics = 44
chemistry = 15
maths = 55
# print(physics > 33 and chemistry > 33)
# print(physics > 33 or chemistry > 33)
print(physics > 33 and not chemistry > 33)
print(not (physics > 33 and chemistry > 33))
print(not (physics > 33 or chemistry > 33))
print(physics > 33 and chemistry > 33 or maths > 33)
print(physics > 33 and chemistry > 33 or maths > 33 and chemistry < 33)
print(physics > 33 and chemistry > 33 or maths > 33 and chemistry < 33)
print(maths > 33 and chemistry < 33 or physics > 33 and chemistry > 33)
