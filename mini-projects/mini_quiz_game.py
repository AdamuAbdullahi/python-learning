score = 0
answer1 = input("What is the capital of France?")

if answer1.lower() == "paris":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer2 = input("What is 5 + 3?")

if answer2 == "8":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer3 = input("What color is the sky? ")

if answer3.lower() == "blue":
    print("Correct!")
    score += 1
else:
    print("Wrong!")
print("Your final score is:", score, "/ 3")