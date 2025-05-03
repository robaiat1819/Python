""" Function - kargs """

def full_name(first,last):
    name = f'{first} {last}'
    return name
# take parmeters in order (serial wise)
name = full_name('Alu','kodu')
# take a parameters in  
name = full_name(last='Alu',first='kodu')
print(name)


def famous_name(first,last,title,addition):
    name = f'{title},{first},{last}'
    return name
name = famous_name(first='taher',last='Ali',title='hujur',addition='taheri')
print(name)

# return mutliple thing from an array 

def a_lot(num1,num2):
    sum = num1+num2
    multi = num1+num2
    reamin = num1-num2
    # return [sum,multi,reamin]
    return sum,multi,reamin
everything = a_lot(40,50)
print(everything)