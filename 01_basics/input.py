name = input("Enter your name: ")
print(f"Hello, {name}")

age = int(input("Enter your age: "))
print(f"Next year you will be {age + 1}")

price = float(input("Enter price: "))
tax = price * 0.1
print(f"Price with tax: {price + tax:.2f}")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(f"Sum: {a + b}")
print(f"Product: {a * b}")
print(f"Greater: {a if a > b else b}")
