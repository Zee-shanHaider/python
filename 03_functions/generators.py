def count_up(n):
    i = 0
    while i < n:
        yield i
        i += 1

for val in count_up(5):
    print(val)

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
for _ in range(10):
    print(next(fib), end=" ")
print()

def squares(n):
    for i in range(n):
        yield i ** 2

gen = squares(5)
print(next(gen))
print(next(gen))
print(list(gen))

sq = (x ** 2 for x in range(10))
print(sum(sq))

def read_in_chunks(data, size):
    for i in range(0, len(data), size):
        yield data[i:i + size]

for chunk in read_in_chunks("PythonGenerators", 4):
    print(chunk)
