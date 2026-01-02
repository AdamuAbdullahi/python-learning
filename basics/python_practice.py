name = input("Enter your name: ")
age = input("Enter your age: ")

print("Hello", name + ", you are", age, "years old.")

num = int(input("Enter a number: "))

if num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter  second number: "))

sum_result = num1 + num2
print("The sum is:", sum_result)

age = int(input("Enter your age: "))
if age < 13:
    print("You are a Child")
elif 13 <= age <= 19:
    print("You are a Teenager")
else:
    print("You are an Adult")

celsius = float(input("Enter temperature in Celsuis: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)

num = int(input("Enter a number: "))

print(f"\nMultiplication Table for {num}:")
for i in range(1, 10 + 1):
    print(f"{num} * {i} = {num * i}")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

largest = a

if b > largest:
    largest = b
if c > largest:
    largest = c

print("The largest number is:", largest)

year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a leap year")
else:
    print(year, "is Not a leap year")

correct_username = "admin"
correct_password = "12345"

username = input("Enter username:")
password = input("Enter password:")

if username == correct_username and password == correct_password:
    print("Login successful!")
else:
    print("Login failed!")

word = input("Enter a word: ")
vowels = "aeiouAEIOU"
count = 0

for letter in word:
    if letter in vowels:
        count += 1

print("Number of vowels:", count)

tasks = []

while True:
    task = input("Enter a task (or type 'exit' to stop): ")
    if task.lower() == "exit":
        break
    tasks.append(task)

print("\nYour tasks:")
for t in tasks:
    print("-", t)

import random

secret = random.randint(1, 10)

guess = int(input("Guess a number between 1 and 10: "))

if guess == secret:
    print("Correct! You guessed it!")
else:
    print("Wrong! The number was", secret)


word = input("Enter a word: ")

reversed_word = ""
for char in word:
    reversed_word = char + reversed_word

print("Reversed:", reversed_word)

word = input("Enter a word: ")

vowels = "aeiouAEIOU"
count = 0

for char in word:
    if char in vowels:
        count += 1

print("Vowel count:", count)

def add (a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    return a / b

print("Choose operation: +, -, *, /")
op = input("Operator: ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if op == "+":
    print("Result:", add(num1,num2))
elif op == "-":
    print("Result:", subtract(num1,num2))
elif op == "*":
    print("Result:", multiply(num1,num2))
elif op == "/":
    print("Result:", divide(num1,num2))
else:
    print("Invalid operator!")

sentence = input("Enter a sentence: ")

words = sentence.split()
count = len(words)

print("Number of words:", count)