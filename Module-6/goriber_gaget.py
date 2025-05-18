class Laptop:
    def __init__(self, brand, price, colour, memory):
        self.brand = brand
        self.price = price
        self.colour = colour
        self.memory = memory

    def run(self):
        return f"Runnig laptop: {self.brand}"

    def coding(self):
        return f"learing python and practing"

    def phone_cal(self, numer, text):
        return f"sendig sms to : {numer} with : {text}"


class Phone:
    def __init__(self, brand, colour, price, dual_sim):
        self.brand = brand
        self.colour = colour
        self.price = price
        self.dual_sim = dual_sim


class Camera:
    def __init__(self, brand, price, colour, pixel):
        self.brand = brand
        self.price = price
        self.colour = colour
        self.pixel = pixel

    def run(self):
        pass

    def change_lens(self):
        pass
