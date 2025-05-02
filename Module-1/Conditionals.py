# in , not , not in, is , not is 
# > , < , >= , <= , == , ==!

boss = False

a = int(input("valu of a : "))
if a>5:
    print("5 er cheye boro ")
    print("koto beshi ke jane")
    
elif a>3:
    print('olpo boro ')
else:
    print("chooto chooto rate lombi hoye")



if boss == True:
    print('tel er basko niye aitaci boss re tel dimu')
else:
    print('lunch er pore ashen')
    
    
# Nested Condition
coin = 'head'

if boss == True:
    print('boss you are joss')
    if coin== 'tail':
        print('batting')
    else:
        print('bowling')
        if 5 > 2 :
            print('do something ')
            if 8%2 == 0 and 5%2 == 1:
                print('even 8 is even number')
else:
    print('you are loss not a boss')