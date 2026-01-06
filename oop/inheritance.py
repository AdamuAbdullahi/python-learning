class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name}")
        print(f"I am {self.age} years old")

class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def introduce(self):
        super().introduce()
        print(f"I study {self.course}")

student1 = Student("Adam", 21, "Data Science")
student1.introduce()

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def introduce(self):
        super().introduce()
        print(f"I teach {self.subject}")

teacher1 = Teacher("John", 35, "Mathematics")
teacher1.introduce()