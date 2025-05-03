numbers = [10,11,14,15,18,20,30,40]
odds = []
for num in numbers:
    if num % 2 == 1:
        odds.append(num)


print(odds)

odds_num = [num for num in numbers if num % 2 == 1]
print(odds_num)

players = ['sakib', 'musfik','liton']
ages = [38, 38, 32]
age_comb = []
for player in players:
    print('player',player)
    for age in ages:
        print(player,age)
        age_comb.append([player,age])

print(age_comb)


# Quiz Code 
"""
def solve(a, b):
    return a**b
    
result = solve(2, 4)
print(result)

def display_person(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")


display_person(Name="Amir Khan", Age="45")

numbers =[7,8,5,4,3,2,4]
print(numbers[::-1])
"""

