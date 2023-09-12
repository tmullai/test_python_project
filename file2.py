# Python program to find the minimum of two numbers


def minimum(a, b):
    if a >= b:
        return b
    else:
        return a

 
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
print("Minimum value = ", minimum(a, b))

