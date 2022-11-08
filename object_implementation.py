class Employee:
    def __init__(self, a, b, c):
        self.id = a
        self.name = b
        self.salary = c
    def display(self):
        print("Employee id is = ", self.id)
        print("Employee name is = ", self.name)
        print("Employee salary is = ", self.salary)

e1 = Employee(12105973, "Harsh Sood", 100000)
e1.display()
