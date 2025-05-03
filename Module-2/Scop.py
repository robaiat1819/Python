# balance = 3000

# def buy_thing(item,price):
#     dream_phone = 'xphone'
#     global balance 
#     price(f'previous balance value : {balance}')
#     balance = balance-price
#     price(f'banalnce after buying {item} : {balance}')
# # print(dream_phone)
# buy_thing('sunglass', 1000)

# print('global balance after buy',balance)

balance = 3000

def buy_thing(item, price):
    dream_phone = 'xphone'
    global balance 
    print(f'Previous balance value: {balance}')
    balance = balance - price
    print(f'Balance after buying {item}: {balance}')

buy_thing('sunglass', 1000)
print('Global balance after buy:', balance)
