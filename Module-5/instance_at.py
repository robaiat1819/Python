class shop:
    shoping_mall = "jamuna"

    def __init__(self, buyer):
        self.buyer = buyer
        self.cart = []  # cart is a instance attribute

    def add_to_cart(self, item):
        self.cart.append(item)


mehjabin = shop("meha jabin")
mehjabin.add_to_cart("shoes")
mehjabin.add_to_cart("phone")
print(mehjabin.cart)

niso = shop("nisho")
niso.add_to_cart("cap")
niso.add_to_cart("watch")
print(niso.cart)


apurbo = shop("Agea purbo chilo")
apurbo.add_to_cart("sunglass")
print(apurbo.cart)
