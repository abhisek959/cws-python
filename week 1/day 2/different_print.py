"""
different ways to print a variable
int(%d), float(%f), str(%s), bool


"""
# My name is Abhisek
# My age is 77
name = "Abhisek"
age = 77
gender = "Male"

# Method 1
print("My name is", name)
print("My age is", age)
print("My name is", name, "and my age is", age)

# Method 2
print(f"My name is {name} and my age is {age}")
print(f"{name}{age}")

# Method 3
print("My name is %s" % (name))
print("My name is %s and my age is %d" % (name, age))
print("My name is %d and my age is %s" % (name, age))
