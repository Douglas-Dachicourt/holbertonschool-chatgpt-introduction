#!/usr/bin/python3

class Checkbook:
    def __init__(self):
        # Initial balance set to 0.0
        self.balance = 0.0

    def deposit(self, amount):
        # Validate that the deposit amount is positive
        if amount <= 0:
            print("Error: Deposit amount must be greater than zero.")
            return
        self.balance += amount  # Update balance with the deposited amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        # Ensure the withdrawal amount is positive and not exceeding the balance
        if amount <= 0:
            print("Error: Withdrawal amount must be greater than zero.")
            return
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount  # Deduct from the balance
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        # Display the current balance
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    # Create a new instance of Checkbook
    cb = Checkbook()
    # Main loop for user input
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").lower()
        if action == 'exit':
            print("Exiting the program. Goodbye!")
            break  # Exit the loop to end the program
        elif action == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number for the deposit.")
        elif action == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number for the withdrawal.")
        elif action == 'balance':
            cb.get_balance()  # Display the current balance
        else:
            print("Invalid command. Please try again.")  # Handle invalid input

if __name__ == "__main__":
    main()