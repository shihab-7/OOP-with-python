class User:
    account_number = 1
    users = []

    def __init__(self, name, email, address, account_type):
        self.account_number = User.account_number
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.transactions = []
        self.loans_taken = 0

        User.account_number += 1
        User.users.append(self)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited ${amount}")
            print(f"Deposited ${amount} into Account {self.account_number}")
        else:
            print("Invalid amount for deposit.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrew ${amount}")
            print(f"Withdrew ${amount} from Account {self.account_number}")
        elif amount > self.balance:
            print("Withdrawal amount exceeded.")
        else:
            print("Invalid amount for withdrawal.")

    def check_balance(self):
        print(f"Account {self.account_number} balance: ${self.balance}")

    def check_transaction_history(self):
        print(f"Transaction history for Account {self.account_number}:")
        for transaction in self.transactions:
            print(transaction)

    def take_loan(self, amount):
        if self.loans_taken < 2 and amount > 0:
            self.loans_taken += 1
            self.balance += amount
            self.transactions.append(f"Loan of ${amount} taken")
            print(f"Loan of ${amount} credited to Account {self.account_number}")
        elif self.loans_taken >= 2:
            print("You have already taken the maximum number of loans (2).")
        else:
            print("Invalid loan amount.")

    def transfer(self, target_account, amount):
        if target_account in User.users:
            if amount > 0 and amount <= self.balance:
                target_account.deposit(amount)
                self.balance -= amount
                self.transactions.append(f"Transferred ${amount} to Account {target_account.account_number}")
                print(f"Transferred ${amount} to Account {target_account.account_number}")
            else:
                print("Invalid amount for transfer.")
        else:
            print("Account does not exist.")

    def __str__(self):
        return f"Account Number: {self.account_number}\nName: {self.name}\nEmail: {self.email}\nAddress: {self.address}\nAccount Type: {self.account_type}\n"

class Admin:
    def create_user(self, name, email, address, account_type):
        User(name, email, address, account_type)
        print(f"User account for {name} created successfully.")

    def delete_user(self, account_number):
        for user in User.users:
            if user.account_number == account_number:
                User.users.remove(user)
                print(f"User account {account_number} has been deleted.")
                return
        print(f"User account {account_number} not found.")

    def list_all_users(self):
        for user in User.users:
            print(user)

    def total_balance(self):
        total = sum(user.balance for user in User.users)
        print(f"Total available balance in the bank: ${total}")

    def total_loan_amount(self):
        total_loans = sum(user.balance for user in User.users if user.loans_taken > 0)
        print(f"Total loan amount in the bank: ${total_loans}")

    def toggle_loan_feature(self, enable=True):
        if enable:
            User.loans_taken = 2
            print("Loan feature is enabled.")
        else:
            User.loans_taken = 0
            print("Loan feature is disabled.")

if __name__ == "__main__":
    admin = Admin()

    while True:
        print("\nWelcome to the Banking Management System")
        print("1. User Operations")
        print("2. Admin Operations")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            print("\nUser Operations:")
            print("1. Create Account")
            print("2. Login")
            print("3. Back to Main Menu")
            user_choice = input("Enter your user_choice: ")

            user_choice = input("Enter your choice: ")

            if user_choice == '1':
                name = input("Enter your name: ")
                email = input("Enter your email: ")
                address = input("Enter your address: ")
                account_type = input("Enter your account type (Savings/Current): ").capitalize()

                admin.create_user(name, email, address, account_type)
            elif user_choice == '2':
                account_number = input("Enter your account number: ")
                user = None
                for u in User.users:
                    if u.account_number == int(account_number):
                        user = u
                        break
                if user:
                    while True:
                        print("\nUser Menu:")
                        print("1. Deposit")
                        print("2. Withdraw")
                        print("3. Check Balance")
                        print("4. Check Transaction History")
                        print("5. Take a Loan")
                        print("6. Transfer Money")
                        print("7. Logout")
                        user_option = input("Enter your choice: ")

                        if user_option == '1':
                            amount = float(input("Enter the deposit amount: "))
                            user.deposit(amount)
                        elif user_option == '2':
                            amount = float(input("Enter the withdrawal amount: "))
                            user.withdraw(amount)
                        elif user_option == '3':
                            user.check_balance()
                        elif user_option == '4':
                            user.check_transaction_history()
                        elif user_option == '5':
                            amount = float(input("Enter the loan amount: "))
                            user.take_loan(amount)
                        elif user_option == '6':
                            target_account_number = int(input("Enter the target account number: "))
                            target_user = None
                            for u in User.users:
                                if u.account_number == target_account_number:
                                    target_user = u
                                    break
                            if target_user:
                                amount = float(input("Enter the transfer amount: "))
                                user.transfer(target_user, amount)
                            else:
                                print("Account does not exist.")
                        elif user_option == '7':
                            break
                        else:
                            print("Invalid choice. Please try again.")
            elif user_choice == '3':
                continue
            else:
                print("Invalid choice. Please try again.")
        elif choice == '2':
            print("\nAdmin Operations:")
            print("1. Delete User Account")
            print("2. List All Users")
            print("3. Check Total Available Balance")
            print("4. Check Total Loan Amount")
            print("5. Toggle Loan Feature")
            print("6. Back to Main Menu")
            admin_choice = input("Enter your choice: ")

            if admin_choice == '1':
                account_number = int(input("Enter the account number to delete: "))
                admin.delete_user(account_number)
            elif admin_choice == '2':
                admin.list_all_users()
            elif admin_choice == '3':
                admin.total_balance()
            elif admin_choice == '4':
                admin.total_loan_amount()
            elif admin_choice == '5':
                loan_feature = input("Do you want to enable the loan feature? (yes/no): ")
                if loan_feature.lower() == "yes":
                    admin.toggle_loan_feature(True)
                else:
                    admin.toggle_loan_feature(False)
            elif admin_choice == '6':
                continue
            else:
                print("Invalid choice. Please try again.")
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


