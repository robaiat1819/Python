def call():
    print('calling somone but i dont know')
    return 'cal done'


class phone:
    price = 12000
    coulour = 'blue'
    features = ['camera','speaker','hamer']
    brand = 'samsung'
    
    def call(self):
        print('caling one person')
    
    def send_sms(self,phone,sms):
        text = f'sending sms to:{phone} and message : {sms}'
        return text

my_phone = phone()
print(my_phone.features)
print(my_phone.coulour)
my_phone.call()
result = my_phone.send_sms(41524,'i miss to miss you')
print(result)