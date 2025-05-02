# a = 10
# b = 12
# print(id(a))
# print(id(b))


"""
1. Clas and object 2tai memory consume kore ??   "Interview Question"

1.Ans : class kokono memory consume kore na . Object memory consume kore

immutable : String ()
mutable : list ()

2.different between List and tuple?
Ans: List is mutable (Updatable) and   Tuple is not Updatable.
"""

# List Updating - 

# c = "karim"
# c = list(c)
# c[0] ='F'
# c = "".join(c)
# print(c)

# 2nd Highest value in sorted List-

list1 = [1,2,3,3,3,3,3,3,4,4,5,5,5,6,5,5,7,8]
print(list1[-2])
list1 = set(list1)
list1 = list(list1)
print(list1)

#List revers

list1 = list1[::-1]
print(list1)


#palindrom Python

# a = "madam"
# print(a==a[::-1])

#enumerate 

# for i,j in enumerate(list1):
#     print(i,j)


#list Comprehension -
dictt = {item:list1.count(item) for item in list1}
print(dictt)


value = 5
new_list = [i for i,j in enumerate(list1) if j>value]
print(new_list)



dict1 = {'rahim' : 10, 'Karim' : 20, 'fahim' : 4}
dict2 = {'rahim' : 12, 'karim' : 2, 'sarder' : 20}

result = dict1
for key, value in dict2.items():
    result[key] = result.get(key,0)+value
print(result)

# print(dict2.keys())
# print(dict2.values())
# print(dict2.keys())
