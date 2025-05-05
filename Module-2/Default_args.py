# def sum(num1,num2,num3=0):
#     result = num1+ num2+num3
#     return result
# total = sum(11,99,30)
# print('Total value ',total)

#args
# def all_sum(num1,num2 ,*numbers):
#     print(numbers)
#     # return numbers
#     sum = 0
#     for num in numbers:
#         print(num)
#         sum = sum+ num
#     return sum
# total = all_sum(45,20,30,40, 50,80,48 ,55,66)
# print('total sum' ,total)


# def do_a_lot(*args):
# default Paramneter *args
    
def all_add(*f):
    # print(numbers)
    sum= 0
    for num in f:
        # print(num)
        sum= sum+num
    return sum
result1 = all_add(10,20,30,40,60,30 ,40 ,60)
print(result1)


def mysum(*s):
    sum= 0 
    for num in s:
        sum = sum+num
    return sum
total_sum = mysum(10,20,30,40,50)
print(total_sum)


def summ(a,b):
    result_sum = a+b
    return result_sum
sum_result = sum(10,30)

print(sum_result)

