class Student(object):
    def __init__(self, name):
        self.name = name
 
    def getName(self):
        return self.name
 
    def isStudying(self):
        return False
 
class Record(Student):
    def isStudying(self):
        return True

s1 = Student("Harsh Sood")  
print(s1.getName(), s1.isStudying())
 
s1 = Record("Ankit")  
print(s1.getName(), s1.isStudying())
