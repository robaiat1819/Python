# set  : a unique item collection .No Duplicate and it define set{}
# list : List is a mutable and define it list[]
# tuple: a tuple is immutable and not change data ,it define tuple()

# numbers = [1,2,3,4,5,6,4,6,7,8]
# print(numbers)
# numbers_set = set(numbers)
# print(numbers_set)

# numbers_set.add(55)
# numbers_set.add(56)
# print(numbers_set)

# numbers_set.remove(56)
# print(numbers_set)
# print("after loop")

# for item in numbers_set:
#     print(numbers_set)
# if 9 in numbers_set:
#     print('9 is exist')
# elif 56 in numbers_set:
#     print("56 is exist")
a = {1,2,3}
b = {1,2,3,4,5,1,5,40,30,21}
print(a & b)
print(a | b)

print(b)