for i in range(5):
    print(i)

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

for i in range(1, 11):
    if i % 2 == 0:
        print(i)

count = 0
while count < 5:
    print(count)
    count += 1

for i in range(10):
    if i == 3:
        continue
    if i == 7:
        break
    print(i)

for i in range(3):
    for j in range(3):
        print(i, j)

squares = [x ** 2 for x in range(1, 6)]
print(squares)

evens = [x for x in range(20) if x % 2 == 0]
print(evens)
