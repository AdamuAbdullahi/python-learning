person = {
    "name": "Adam",
    "age": 20,
    "country": "Nigeria"
}

print("Name:", person["name"])
print("Age:", person["age"])
print("Country:", person["country"])
person["age"] = 25
person["country"] = "Ghana"

print("Updated age:", person["age"])
print("Updated country:", person["country"])
person["grade"] = "A"
print("Grade:", person["grade"])

student = {}

student["name"] = input("Enter your name: ")
student["age"] = input("Enter your age: ")
student["course"] = input("Enter your course: ")

print("/nStudent Details:")
print("Name:", student["name"])
print("Age:", student["age"])
print("Course:", student["course"])
