
class User:
    def __init__(self, user_id, pin):
        self.user_id = user_id
        self.pin = pin
        self.balance = 0 
        self.transaction_history = []

    def authenticate(self, user_id, pin):
        return self.user_id == user_id and self.pin == pin

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited ${amount}")
        return self.balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount}")
            return self.balance
        else:
            return "Insufficient funds"

    def transfer(self, recipient, amount):
        if amount <= self.balance:
            self.balance -= amount
            recipient.balance += amount
            self.transaction_history.append(f"Transferred ${amount} to {recipient.user_id}")
            recipient.transaction_history.append(f"Received ${amount} from {self.user_id}")
            return self.balance
        else:
            return "Insufficient funds"


class ATM:
    def __init__(self):
        self.users = {}

    def add_user(self, user_id, pin):
        if user_id not in self.users:
            self.users[user_id] = User(user_id, pin)
            return True
        else:
            return False

    def authenticate_user(self, user_id, pin):
        if user_id in self.users:
            return self.users[user_id].authenticate(user_id, pin)
        else:
            return False

    def get_user_balance(self, user_id):
        return self.users[user_id].balance if user_id in self.users else None

    def get_user_transaction_history(self, user_id):
        return self.users[user_id].transaction_history if user_id in self.users else None



atm = ATM()


atm.add_user("407", "1800")


def show_menu():
    print("\nATM Menu:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Transfer")
    print("4. Check Balance")
    print("5. Transaction History")
    print("6. Quit")



user_id = input("Enter user ID: ")
pin = input("Enter PIN: ")
if atm.authenticate_user(user_id, pin):
    print("Authentication successful")
    user = atm.users[user_id]

    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            amount = float(input("Enter deposit amount: $"))
            print("New balance:", user.deposit(amount))
        elif choice == "2":
            amount = float(input("Enter withdrawal amount: $"))
            print(user.withdraw(amount))
        elif choice == "3":
            recipient_id = input("Enter recipient's user ID: ")
            if recipient_id in atm.users:
                recipient = atm.users[recipient_id]
                amount = float(input("Enter transfer amount: $"))
                print("New balance:", user.transfer(recipient, amount))
            else:
                print("Recipient not found.")
        elif choice == "4":
            print("Your balance is:", user.balance)
        elif choice == "5":
            transaction_history = atm.get_user_transaction_history(user_id)
            if transaction_history:
                print("Transaction History:")
                for transaction in transaction_history:
                    print(transaction)
            else:
                print("No transaction history available.")
        elif choice == "6":
            print("Thank you for using the ATM!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

else:
    print("Authentication failed")
