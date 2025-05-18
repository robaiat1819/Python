# Ena Poribohon


class Company:
    def __init__(self, name, addres):
        self.name = name
        self.addres = addres
        self.bus = []
        self.routes = []
        self.counter = []
        self.drivers = []
        self.manager = []
        self.supervisor = []
        self.fare = []


class Driver:
    def __init__(self, name, licence, age):
        self.name = name
        self.licence = licence
        self.age = age


class Counter:
    def __init__(self):
        pass

    def purhchase_a_ticket(self, start, destination):
        pass


class Passenger:
    pass


class Suppervisor:
    pass


red_mia = Driver("a", "1234", "aaaa")
