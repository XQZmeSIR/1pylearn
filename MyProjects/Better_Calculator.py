# Building a Better Calculator

num1 = float(input('Enter first number: '))   # * Variable for input
op = input('Enter operator: ')                # * Variable for op input
num2 = float(input('Enter second number: '))  # * Variable for second input

if op == "+":           # * Each of If statement identifies operator and use it for
    print(num1 + num2)  # * for diferent operations such as [ +, -, *, / ]
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid operator.")
