name = input("Enter student name: ")
age = int(input("Enter student age: "))
course = input("Enter student course: ")

student = {
    "name": name,
    "age": age,
    "course": course
}

print("\nStudent Information")
print("Name:", student["name"])
print("Age:", student["age"])
print("Course:", student["course"])

if student["age"] < 13:
    print("Category: Child")
elif student["age"] <= 19:
    print("Category: Teenager")
else:
    print("Category: Adult")