def sum(num1,num2,num3=0):
    result = num1+ num2+num3
    return result
total = sum(11,99,30)
print('Total value ',total)

#args
def all_sum(num1,num2 ,*numbers):
    print(numbers)
    # return numbers
    sum = 0
    for num in numbers:
        print(num)
        sum = sum+ num
    return sum
total = all_sum(45,20,30,40, 50,80,48 , 55,66)
print('total sum' ,total)


def do_a_lot(*args):
    print(args)