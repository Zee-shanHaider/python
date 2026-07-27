def greet(name):
    return f"Hello, {name}"

print(greet("Zeeshan"))

def add(a, b):
    return a + b

print(add(3, 5))

def power(base, exp=2):
    return base ** exp

print(power(3))
print(power(3, 3))

def total(*args):
    return sum(args)

print(total(1, 2, 3, 4, 5))

def profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

profile(name="Zeeshan", role="Engineer", language="Python")

def multiply(a, b):
    return a * b

double = lambda x: x * 2
square = lambda x: x ** 2

print(double(5))
print(square(4))

numbers = [5, 2, 8, 1, 9, 3]
print(sorted(numbers, key=lambda x: x))

def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

triple = make_multiplier(3)
print(triple(7))
