class Student:
    def __init__(self, id, name="Harsh Sood"):
        self.id = id
        self.name = name
    def getDetails(self):
        print("Employee ID: {}" .format(self.id))
        print("Employee Name: {}" .format(self.name))

s1 = Student(12105973)
s1.getDetails()
s2 = Student(12105974, "Mayank")
s2.getDetails()

