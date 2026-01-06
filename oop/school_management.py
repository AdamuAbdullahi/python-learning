class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def introduce(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def introduce(self):
        super().introduce()
        print(f"Course: {self.course}")

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def introduce(self):
        super().introduce()
        print(f"Subject: {self.subject}")

student1 = Student("Adam", 21, "Data Science")
teacher1 = Teacher("John", 35, "Mathematics")

print("Student Info:")
student1.introduce()

print("\nTeacher Info:")
teacher1.introduce()