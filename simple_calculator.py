num1 = float(input("Enter the first number: "))
op = input("Enter the operation (+, -, *, /): ")
num2 = float(input("Enter the second number: "))
if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    result = num1 / num2
else:
    result = "Invalid operation"

print(f"The result is {result}")
