import random

class Account:
    def __init__(self, account_number, name, balance: float):
        self.account_name = account_number
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"Account owner: {self.name}\nNumber: {self.account_name}\nBalance: ${self.balance}"

class Bank:
    def __init__(self):
        self.accounts = {}  # Corrected dictionary initialization
        self.filename = "accounts.txt"
        self.load_from_file()

    def create_account(self, name, initial_deposit):
        """
        You can create new account with this function
        """
        try:
            while True:
                acc_num = self.generate_number()
                if acc_num not in self.accounts:
                    break

            self.accounts[acc_num] = Account(acc_num, name, initial_deposit)
            print(f"Account successfully created!\n{self.accounts[acc_num]}")
        except Exception as e:
            print(f"Error has occurred: {e}")

    def view(self):
        for account in self.accounts.values():
            print(account)

    def view_account(self):
        """
        This function let user to view account info
        """
        try:
            account_number = int(input("Enter your account: "))
            if account_number not in self.accounts:
                print("Account not found!")
                return False
            print(self.accounts[account_number])
            return True
        except ValueError:
            print("Invalid input. Account number must be an integer.")

    def deposit(self):
        """
        Prompts a user to enter their account and amount
        Then if account exist value is validated and update the balance 
        """
        try:
            account_number = int(input("Enter your account number: "))
            amount = float(input("Enter deposit amount: "))

            if amount < 0:
                raise ValueError("Amount cannot be negative.")
            if account_number not in self.accounts:
                raise ValueError("Account not found. Please enter a valid account number.")
            
            self.accounts[account_number].balance += amount
            print(f"Deposit successful! New balance: ${self.accounts[account_number].balance}")
        except ValueError as e:
            print(f"Error: {e}")

    def withdraw(self):
        """
        Prompts a user to eneter their account and amount
        Withdraws amount from account if amount is less than balance and valid
        """
        try:
            account_number = int(input("Enter your account number: "))
            amount = float(input("Enter withdrawal amount: "))

            if amount < 0:
                raise ValueError("Amount cannot be negative.")
            if account_number not in self.accounts:
                raise ValueError("Account not found. Please enter a valid account number.")

            balance = self.accounts[account_number].balance
            if balance < amount:
                raise ValueError(f"Insufficient funds! Your balance is ${balance}")

            self.accounts[account_number].balance -= amount
            print(f"Withdrawal successful! New balance: ${self.accounts[account_number].balance}")
        except ValueError as e:
            print(f"Error: {e}")

    def save_to_file(self):
        """
        Use `save_to_file` to write account details to `accounts.txt`.
        """
        try:
            with open(self.filename, mode="w") as file_handler:
                for account in self.accounts.values():
                    file_handler.write(f"{account.account_name},{account.name},{account.balance}\n")
            print("Accounts saved successfully.")
        except Exception as e:
            print(f"Error writing to file: {e}")

    def load_from_file(self):
        """
        Use `load_from_file` to load account details when the program starts.
        """
        self.create_file()
        try:
            with open(self.filename) as file_handler:
                for line in file_handler:
                    acc = line.strip().split(',')
                    if len(acc) == 3:
                        self.accounts[int(acc[0])] = Account(int(acc[0]), acc[1], float(acc[2]))
            print("Accounts loaded successfully.")
        except Exception as e:
            print(f"Error loading from file: {e}")

    def create_file(self):
        try:
            with open(self.filename, "r") as file:
                file.read()
        except FileNotFoundError:
            with open(self.filename, "w") as file:
                file.write("")

    def generate_number(self):
        return random.randint(10**15, 10**16 - 1)

if __name__ == "__main__":
    bank = Bank()
    bank.create_account("Mirzabek", 200)
    bank.view()
    bank.save_to_file()
