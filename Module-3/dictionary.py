numbers = [1,2,3,4,5,8,7,11,9]
person1 = ['kala chan','kalipur',23, 'student']

# key value pair 
# Dictionary 

person = {'name ': 'khala paki', 'addres': 'kalipur','job': 'facebooker','age': '23'}
print(person)
print(person['job'])
print(person['age'])
print(person.keys())
print(person.values())
person['language'] = 'python'
person['name '] = 'sada pakhi'
print(person)
del person['age']
print(person)

# special dictionary looping 
for key,Value in person.items():
    print(key,Value)