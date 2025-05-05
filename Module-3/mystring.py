name = 'Sakib\'s Khan'  # escape
name2 = "Sakib Khan"
name3 = """
    Shakib Khan
    Number one 
"""


print(name3)
print(name)

# for char in name2:
#     print(char)
    
print(name2[3])
print(name2[1:7])
print(name2[-3])
print(name2[::-1])

# name2[0] = "R"
print(name2)


if 'Khan' in name2:
    print('exist')

print(name2.upper())

# revision Practice String -

sentence = "robaiat hossain fardin"

capitalized_string = sentence.capitalize()

print(sentence)

print(capitalized_string)

new_string = sentence.center(24,'*')
print(new_string)  
