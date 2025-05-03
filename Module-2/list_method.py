numbers = [10, 20, 30, 50, 45, 60]

numbers.append(100)
print(numbers)

numbers.insert(6, 99)
print(numbers)

numbers.remove(100)
print(numbers)

if 60 in numbers:
    numbers.remove(60)
print(numbers)

if 33 in numbers:
    numbers.remove
print(numbers)

last = numbers.pop()
print(last,numbers)


index = numbers.index(45)
print(index)

sorted = numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)