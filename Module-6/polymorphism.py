# Poly ---> Many (Multiple)
# Morph ---> Shap


class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("animal making some sound mew mew")


class cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        print("mew mew")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        print("gew gew ")


class Goat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        print("hu hu hu hu")


don = cat("real")
don.make_sound()
shaerd = Dog("Local shaperd")
shaerd.make_sound()
messi = Goat("Lionel Messi")
messi.make_sound()
less = Goat("gora gori , Nymar")

animals = [don, shaerd, messi, less]

for animal in animals:
    animal.make_sound()
