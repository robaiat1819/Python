class shoping:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, item, price, quantity):
        product = {"item": item, "price": price, "quantity": quantity}
        self.cart.append(product)
    
    # Home work for me !!!
    def remove_item(self,item):
        pass
    


    def cheekout(self, amount):
        total = 0
        for item in self.cart:
            # print(item)
            total += item["price"] * item["quantity"]
        print("total price ", total)
        if amount < total:
            print(f"pleas provide {total-amount} more")
        else:
            extra = amount - total
            print(f"Here is your item and extra {extra}")


swapan = shoping("alan swapon")
swapan.add_to_cart("alu", 12, 24)
swapan.add_to_cart("dim", 55, 10)
swapan.add_to_cart("moric", 44, 90)
print(swapan.cart)
swapan.cheekout(5500)
