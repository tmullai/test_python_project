# Python program to find the maximum of two numbers


def maximum(a, b):
    if a >= b:
        return a
    else:
        return b

 
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
print(maximum(a, b))
