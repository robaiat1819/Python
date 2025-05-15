class shop:
    cart = [] # is class attribute 

    def __init__(self, buyer):
        self.buyer = buyer

    def add_to_cart(self, item):
        self.cart.append(item)


mehjabin = shop("meh jaben")
mehjabin.add_to_cart("shoes")
mehjabin.add_to_cart("phone")
print(mehjabin.cart)


niso = shop("niso")
niso.add_to_cart("cap")
niso.add_to_cart("Watch")
print(niso.cart)
