class phone:
    manufactured = "China"

    def __init__(self, owner, brand, price):
        self.owner = owner
        self.brand = brand
        self.price = price
        pass

    def send_sms(self, phone, sms):
        text = f"sending to: {phone} {sms}"
        print(text)


my_phone = phone("khala chan", "oppo", 9800)
print(my_phone.owner, my_phone.price, my_phone.brand)
her_phone = phone('she jaan','iphone',120000)
print(her_phone.owner,her_phone.brand,her_phone.price)
