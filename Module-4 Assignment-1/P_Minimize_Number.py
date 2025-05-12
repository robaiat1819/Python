n = int(input())
arr = list(map(int, input().split()))

count = 0
while True:
    all_even = True
    for num in arr:
        if num % 2 != 0:
            all_even = False
            break
    if not all_even:
        break
    for i in range(n):
        arr[i] = arr[i] // 2
    count += 1

print(count)
