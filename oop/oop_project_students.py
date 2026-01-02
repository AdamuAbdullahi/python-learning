class Student:
    school = "Global High School"

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        print("Hello, my name is", self.name)
        print("I am", self.age, "years old")
        print("I study", self.course)
        print("School:", self.school)

# Create students
student1 = Student("Adam", 21, "Data Science")
student2 = Student("John", 22, "Mathematics")

# Show info
student1.introduce()
student2.introduce()