person = {
    "name": "Adam",
    "age": 20,
    "country": "Nigeria"
}

print("Name:", person["name"])
print("Age:", person["age"])
print("country:", person["country"])

person["age"] = 25
person["country"] = "Ghana"

print("Updated Age:", person["age"])
print("Updated Country:", person["country"])

person["grade"] = "A"
print("Grade:", person["grade"])

del person["grade"]
print("Person dictionary after deleting grade:", person)

students = {
    "student1": {"name": "Adam", "age": 20},
    "student2": {"name": "John", "age": 22}
}

print(students["student1"]["name"])
print(students["student2"]["age"])

for key, value in person.items():
    print(key, ":", value)

student = {}

student["name"] = input("Enter your name: ")
student["age"] = input("Enter your age: ")
student["course"] = input("Enter your course: ")

print("\nStudent Detials:")
print("Name:", student["name"])
print("Age:", student["age"])
print("Course:", student["course"])