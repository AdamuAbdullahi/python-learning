sentence = input("Enter a sentence: ")
letter = input("Enter a letter to count: ")

count = sentence.lower().count(letter.lower())

print(f"The letter '{letter}' appears {count} times.")
