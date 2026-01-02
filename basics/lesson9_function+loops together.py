def count_to_n(n):
    for i in range(1, n + 1):
        print(i)

# call the function
count_to_n(5)

def print_even_numbers(n):
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(i)

# call the function
print_even_numbers(10)

def repeat_message(message, times):
    for _ in range(times):
        print(message)

# Call the function
repeat_message("Hello from Python!", 3)

def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Call the function
result = sum_list([3, 5, 7, 10])
print("Total:", result)

def multiplication_table(n):
    for i in range(1, 11):
        print(n, "*", i, "=", n * i)

# Call the function
multiplication_table(4)