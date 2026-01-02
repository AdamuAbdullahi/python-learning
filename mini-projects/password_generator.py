import random
import string

length = int(input("Enter password lenght: "))
characters = string.ascii_letters + string.digits + string.punctuation
password = "".join(random.choice(characters) for _ in range(length))

print("Your password is:", password)