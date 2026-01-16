class InsufficientFundsError(Exception):
    pass

balance = 1000

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Choose an option: ")

    try:
        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            if amount <= 0:
                raise ValueError("Deposit must be positive.")
            balance += amount
            print("Deposited:", amount)
            
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            if amount > balance:
                raise InsufficientFundsError("Not enough balance.")
            balance -= amount
            print("Withdrawn:", amount)

        elif choice == "3":
            print("Current balance:", balance)

        elif choice == "4":
            print("Thank you for using the bank system!")
            break

        else:
            print("Invalid option.")

    except ValueError as e:
        print("Error:", e)

    except InsufficientFundsError as e:
        print("Bank Error:", e)