class Student:
    def __init__(self, name, curent_class, id):
        self.name = name
        self.curent_class = curent_class
        self.id = id

    def __repr__(self):
        return f"Student with name : {self.name}, class : {self.curent_class}, id : {self.id}"


class teacher:
    def __init__(self, name, subject, id):
        self.name = name
        self.subject = subject
        self.id = id

    def __repr__(self):
        return f"teacher : {self.name}, subject : {self.subject}, id : {self.id}"


class School:
    def __init__(self, name):
        self.name = name
        self.teachers = []
        self.students = []

    def add_teacher(self, name, subject):
        self.teachers = teacher
        id = len(self.teachers) + 101
        teachers = teacher(name, subject, id)
        self.teachers.append(teachers)

    def enroll(self, name, fee):
        if fee < 6500:
            return f"not enough fee"
        else:
            id = len(self.students) + 1
            student = Student(name, "C", id)
            self.students.append(student)
            return f" {name} is enrolled with id: {id},extra money: {fee-6500}"

    def __repr__(self):
        print("wellcome to ", self.name)
        print("---------Our Teacher----------")
        for teacher in self.teachers:
            print(teacher)
        print("---------Our student--------")
        for student in self.students:
            print(student)


# rahat_khan_patan = teacher("Rahat Khan", "Algorithm", 101)
# alia = Student("alia ", 9, 1)
# print(rahat_khan_patan)
# print(alia)

# phitron = School("phitron")
# phitron.enroll("alia", 7000)
# phitron.enroll("rani", 8000)
# phitron.enroll("aiswhoria", 9000)
# phitron.enroll("vaijan", 10000)
# phitron.add_teacher("cruish", "algo")
# phitron.add_teacher("decap", "ds")
# phitron.add_teacher("aj", "database")
# print(phitron)
