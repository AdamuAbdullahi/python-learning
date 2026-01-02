def greet(name):
    print("Hello", name)
greet("Adam")
greet("John")

def add(a, b):
    return a + b
result = add(5, 7)
print("Sum:", result)

def check_age(name, age):
    if age >= 18:
        return name + " is an adult"
    else:
        return name + " is not an adult"
    
message = check_age("Adam", 20)
print(message)

def welcome(name="Student"):
    print("Welcome", name)

welcome("Adam")
welcome()