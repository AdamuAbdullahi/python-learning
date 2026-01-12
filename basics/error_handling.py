# Example 1: Handle invalid number input
try:
    number = int(input("Enter a number: "))
    print("You entered:", number)
except ValueError:
    print("Invalid input! Please enter a number.")

# Example 2: Handle division errors
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Please enter valid numbers.")

# Example 3: else and finally
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("That was not a number.")
else:
    print("Great! You entered:", number)
finally:
    print("Program finished.")