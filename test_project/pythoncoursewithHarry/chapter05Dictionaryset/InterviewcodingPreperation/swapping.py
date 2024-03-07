# Swapping of two numbers using third variable in Python language
a = int(input("enter first number:"))
b = int(input("enter second number:"))
tempvar = a
a = b
b = tempvar
print("After swapping")
print("value of a is:", a)
print("value of b is:", b)