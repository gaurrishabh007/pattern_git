class Student:
    def __init__(self, x,y,z):
        self.name=x
        self.rollno=y
        self.marks=z

    def display(self):
        print("Student Name:{}\nRollno:{}\nMarks:{}".format(self.name, self.rollno, self.marks))
s1=Student("rishabh", 17, 97)
s1.display()

s2=Student("pandey", 88, 90)
s2.display()
        