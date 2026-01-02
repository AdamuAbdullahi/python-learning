class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print("Withdrawn:", amount)

    def show_balance(self):
        print("Current balance:", self.balance)

account1 = BankAccount("Adam", 1000)

account1.show_balance()
account1.deposit(500)
account1.withdraw(300)
account1.show_balance()


while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Show Balance")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        amount = float(input("Enter amount to deposit: "))
        account1.deposit(amount)

    elif choice == "2":
        amount = float(input("Enter amount to withdraw: "))
        account1.withdraw(amount)

    elif choice == "3":
        account1.show_balance()

    elif choice == "4":
        print("Thank you for using the bank system!")

    else:
        print("Invalid choice!")