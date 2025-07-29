def add(a, b):
    return a + b

def minus(a, b):
    return a - b

def product(a, b):
    return a * b

def division(a, b):
    return a / b

a= int(input("Enter first number: "))
b= int(input("Enter second number: "))


print("Addition: ", add(a, b))
print("Subtraction: ", minus(a, b))
print("Multiplication: ", product(a, b))
print("Division: ", division(a, b))