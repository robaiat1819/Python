class Family:
    def __init__(self, addres):
        self.addres = addres


class School:
    def __init__(self, id, level):
        self.id = id
        self.level = level


class Sport:
    def __init__(self, game):
        self.game = game


class Student(Family, School, Sport):

    def __init__(self, addres, id, level, game):
        School.__init__(self, id, level)
        Sport.__init__(self, game)
        Family.__init__(self, addres)
        super().__init__(addres)
