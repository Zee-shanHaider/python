from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squared = list(map(lambda x: x ** 2, numbers))
print(squared)

names = ["zeeshan", "ahmed", "ali"]
capitalized = list(map(str.capitalize, names))
print(capitalized)

evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)

above_five = list(filter(lambda x: x > 5, numbers))
print(above_five)

total = reduce(lambda a, b: a + b, numbers)
print(total)

product = reduce(lambda a, b: a * b, [1, 2, 3, 4, 5])
print(product)

result = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
print(result)
