# list , array , collection are same( simple terms)
#  index = 0   1   2   3   4   5   6   7   
numbers = [10, 11, 12, 13, 14, 15, 16, 17]
#index =  -8  -7   -6  -5 -4  -3  -2  -1
print(numbers[3],numbers[-3])
#list start end (start from start index and end the before of )
print(numbers[0:6])
print(numbers[1:7])

# list ( start end step )
print(numbers[1:7:1])
print(numbers[1:7:2])
print(numbers[2:7:-1])
print(numbers[7:2:-1])
print(numbers[:6])
print(numbers[1:])
print(numbers[:])
print(numbers[::-1])