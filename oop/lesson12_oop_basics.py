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

student1 = Student("Adam", 21, "Data Science")
student1.introduce()
student2 = Student("John", 22, "Mathematics")
student2.introduce()

print(student1.school)
print(student2.school)

print("\nUpdate student1 details")

student1.name = input("Enter your name: ")
student1.age = int(input("Enter your age: "))
student1.course = input("Enter new course: ")

print("\nUpdated student1 information:")
student1.introduce()