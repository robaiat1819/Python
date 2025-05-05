# lambda
# def double (x):
#     return x*2

doubled = lambda num : num *2
squared = lambda num : num* num
output = squared(9)
result = doubled(44)
print(result,output)

add = lambda x,y : x+y
sum = add(11,22)
print(sum)

numbers = [1,2,3,4,5,6,4,6,7,8]
# doubled_nums = map(doubled,numbers)
doubled_nums = map(lambda x: x*2, numbers)
print(numbers)
print(list(doubled_nums))

actors = [
    {'name ': 'sabhana','age': '65'},
    {'name ': 'porimoni ','age': '36'},
    {'name ': 'sabila nur' , 'age': '35'},
    {'name ': 'shawn', 'age': '35'}
]

junior = filter(lambda actor : actor ['age']<40, actors)
# junior= list(junior)
print(list(junior))
