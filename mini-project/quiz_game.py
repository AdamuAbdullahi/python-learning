# Quiz questions
questions = {
    "What is the capital of France?": "Paris",
    "What is 5 + 7? ": "12",
    "Which language is this program written in? ": "Python"
}

score = 0

for question, answer in questions.items():
    user_answer = input(question)
    if user_answer.strip().lower() == answer.lower():
        print("Correct!")
        score += 1
    else:
        print("Wrong! The correct answer is", answer)

print(f"Your total score is: {score}/{len(questions)}")

# Save score to file
with open("quiz_scores.txt", "a") as file:
    file.write(f"Score: {score}/{len(questions)}\n")

print("Your score has been saved to 'quiz_scores.txt'.")