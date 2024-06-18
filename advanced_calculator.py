import math

def add(x, y):
    print("sum\n")
    return x + y

def subtract(x, y):
    print("subtract\n")
    return x - y

def multiply(x, y):
    print("multiplication")
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    return x / y

def exponentiate(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Cannot compute square root of a negative number"
    return math.sqrt(x)

def factorial(x):
    if x < 0:
        return "Factorial is not defined for negative numbers"
    if x == 0 or x == 1:
        return 1
    result = 1
    for i in range(2, x + 1):
        result *= i
    return result

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exponentiate")
print("6. Square Root")
print("7. Factorial")

choice = input("Enter choice (1/2/3/4/5/6/7): ")

if choice in ('1', '2', '3', '4'):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
elif choice in ('5', '6', '7'):
    num1 = float(input("Enter the number: "))

if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))
elif choice == '5':
    print(num1, "^", num2, "=", exponentiate(num1, num2))
elif choice == '6':
    print("Square root of", num1, "=", square_root(num1))
elif choice == '7':
    print("Factorial of", num1, "=", factorial(num1))
else:
    print("Invalid input")
