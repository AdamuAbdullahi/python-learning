import random

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"

length = int(input("Enter the desired password length: "))
password = "".join(random.choice(characters) for _ in range(length))

print("Your generated password is:", password)