class Account:
    def __init__(self, account_number, owner, balance = 0.0):
        self.number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if (amount > 0):
            self.balance += amount
            print(f"Deposited {amount} to {self.number}. Your new balance is {self.balance}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if (amount < 0):
            self.balance -= amount
            print(f"Withdrew {amount} from {self.number}. Your new balance is {self.balance}")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        print(f"Your current balance is ${self.balance}") 
    
    def __str__(self):
        return f"Account[{self.number}] - Owner: {self.owner}, Balance: {self.balance}"

class Bank:
    def __init__(self):
        self.accounts = {}
    
    def create_account(self, account_number, owner):
        if account_number in self.accounts:
            print("Account number already exists.")
        else:
            new_account = Account(account_number, owner)
            self.accounts[account_number] = new_account
            print(f"Account created: {new_account}")

    def get_account(self, account_number):
        return self.accounts.get(account_number)
    
    def deposit_to_account(self, account_number, amount):
        account = self.get_account(account_number)
        if account:
            account.deposit(amount)
        else:
            print("Account not found.")

    def withdraw_from_account(self, account_number, amount):
        account = self.get_account(account_number)
        if account:
            account.withdraw(amount)
        else:
            print("Account not found.")

    def transfer(self, from_account_number, to_account_number, amount):
        from_account = self.get_account(from_account_number)
        to_account = self.get_account(to_account_number)
        if from_account and to_account:
            if amount > 0:
                if amount <= from_account.get_balance():
                    from_account.withdraw(amount)
                    to_account.deposit(amount)
                    print(f"Transferred {amount} from {from_account_number} to {to_account_number}.")
                else:
                    print("Insufficient funds for transfer.")
        else: 
            print("One or both accounts not found.")
    
    def show_accounts(self):
        for account_number, account in self.accounts.items():
            print(account)


def main():
    bank = Bank()

    while True:
        print("""
Banking System Menu:
1. Create account
2. Deposit
3. Withdraw
4. Transfer
5. Show accounts
6. Exit
""")

        choice = input("Enter your choice: ")
        if choice == "1":
            account_number = input("Enter account number: ")
            owner = input("Enter owner name: ")
            bank.create_account(account_number, owner)
        elif choice == "2":
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to deposit: "))
            bank.deposit_to_account(account_number, amount)
        elif choice == "3":
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to withdraw: "))
            bank.withdraw_from_account()
        elif choice == "4":
            from_account_number = input("Enter the account number you want to transfer from: ")
            to_account_number = input("Enter the account number you want to transfer to: ")
            amount = float(input("Enter the amount to transfer: "))
            bank.transfer(from_account_number, to_account_number, amount)
        elif choice == "5":
            bank.show_accounts()
        elif choice == "6":
            print("Thank you for using Elias Banking System! Have a great day!")
            break
        else:
            print("Please enter a valid choice.")

main()
