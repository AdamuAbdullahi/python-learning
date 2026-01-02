student = {}

student["name"] = input("Enter your name: ")
student["age"] = input("Enter your age: ")
student["course"] = input("Enter your course: ")

print("/nStudent Details:")
print("Name:", student["name"])
print("Age:", student["age"])
print("Course:", student["course"])

if int(student["age"]) >= 18:
    print("Your are an adult")
else:
    print("You are a minor")