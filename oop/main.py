from student import Student
from teacher import Teacher

student1 = Student("Adam", 21, "Data Science")
teacher1 = Teacher("John", 35, "Mathematics")

print("Student Info:")
student1.introduce()

print("\nTeacher Info:")
teacher1.introduce()