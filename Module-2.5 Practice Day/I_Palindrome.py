# n = input()
# reversed_n= n==n[::-1].lstrip('0')
# print(reversed_n)

# if n==reversed_n:
#     print(n)
#     print("YES")
# else:
#     print(n)
#     print("NO")


n = input()
reversed_n = n[::-1]
reversed_n_clean = reversed_n.lstrip('0')
print(reversed_n_clean)

if n==n[::-1]:
    print("YES")
else:
    print("NO")
    

