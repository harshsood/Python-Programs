class Person:
    def name(self):
        print("Harsh Sood")
class Teacher(Person):
    def Qualification(self):
        print("Master of Computer Applications")
class HOD(Teacher):
    def experience(self):
        print("2 years")

hod = HOD()
hod.name()
hod.Qualification()
hod.experience()
          
    
