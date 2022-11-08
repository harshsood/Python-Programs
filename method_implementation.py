class Student:
    def __init__(self, a, b, c):
        self.id = a
        self.name = b
        self.univ = c
    def show(self):
        print("Student name is = ", self.name)
    def display(self):
        print("Student id is = ", self.id)
        print("Student studies at = ", self.univ)

s1 = Student(12105973, "Harsh Sood", "Lovely Professional University")
s1.show()
s1.display()
