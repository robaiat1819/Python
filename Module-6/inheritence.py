# Based Class , Parent class,Common Attribute+ Functionality class
# Derieved Class


class Gadegt:
    def __init__(self, brand, price, colour, orgin):
        self.brand = brand
        self.price = price
        self.colour = colour
        self.orgin = orgin

    def run(self):
        return f"Runnig laptop: {self.brand}"


class Laptop:
    def __init__(self, memory, ssd):
        self.memory = memory

    def coding(self):
        return f"learing python and practing"

    def phone_cal(self, numer, text):
        return f"sendig sms to : {numer} with : {text}"


class Phone(Gadegt):
    def __init__(self, brand, price, colour, orgin, dual_sim):
        self.dual_sim = dual_sim

        super().__init__(brand, price, colour, orgin)

    def __repr__(self):
        return f"phone : {self.dual_sim} "

    def __repr__(self):
        return f"phone: {self.brand} {self.price} {self.dual_sim}"


class Camera:
    def __init__(self, pixel):
        self.pixel = pixel

    def change_lens(self):
        pass


# inheritence
# my_phone = Phone("iphone", 120000, "silver", "china", "yes")
my_phone = Phone("iphone", 120000, "silver", "china", True)
print(my_phone)
