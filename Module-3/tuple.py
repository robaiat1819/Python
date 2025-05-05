def multiple():
    return 3,4
print(multiple())

things = 'pen','trypode','Water bottle','phone','charger','web came'
print(things)
print(type(things))
print(things[0])
print(things[-2])
print(things[3:6])

for item in things:
    print(item)

# tuple is immutable - dont't Change value ,
# but they can contain mutable objects

print(len(things))

mega = ([1,3,4,5,6],[2,4,6,8])
print(mega)
print(type(mega))

my_tuple = ('Hello_World')
tuple2 = ('java','python','C','C++')
print(my_tuple)
print(tuple2)
print(type(my_tuple))
