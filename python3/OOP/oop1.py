

class Student:
    def __init__(self, name, age, marks):
        self.name='rishabh'
        self.age=40
        self.marks=80

    def talk(self):
        print("hello i am:", self.name)
        print("my age is:", self.age)
        print("my marks are:", self.marks)

s1=Student("rishabh", 100, 80)
s1.talk()
