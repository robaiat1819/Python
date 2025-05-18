from abc import ABC, abstractmethod

# abc - Abstract Based Class,


class Animal(ABC):
    @abstractmethod  # enforce all derived Class to have a eat method
    def eat(self):
        print("i need food")

    @abstractmethod
    def move(self):
        pass


class Monky(Animal):
    def __init__(self, name):
        self.catagory = "Monky"
        self.name = name
        self.name = "Monky"
        super().__init__()

    def eat(self):
        print("hey nana i am eating banana")

    def move(self):
        print("hanging on the branches")


layka = Monky("lucky")
layka.eat()
print(layka.eat)
