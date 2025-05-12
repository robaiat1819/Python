s = input()
balance = 0
count = 0
current = ""
result = []

for char in s:
    current += char
    if char == "L":
        balance += 1
    else:
        balance -= 1

    if balance == 0:
        count += 1
        result.append(current)
        current = ""

print(count)
for part in result:
    print(part)
