from collections import Counter

n = int(input())
arr = list(map(int, input().split()))


freq = Counter(arr)
removals = 0


for x in freq:
    count = freq[x]
    if count == x:
        continue
    elif count > x:
        removals += count - x
    else:  
        removals += count


print(removals)
