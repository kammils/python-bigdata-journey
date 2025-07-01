# Another example - BankAccount class
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ₹{amount}. New balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("❌ Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Withdrew ₹{amount}. New balance: ₹{self.balance}")

# Extend the BankAccount class from earlier into a SavingsAccount that adds an interest_rate
# and a method add_interest().

class SavingsAccount(BankAccount):

    def add_interest(self):
        print(f"Saving Balance after Year end Interest: {self.balance + self.balance * 18/100}")


# Create an account and test
# account = BankAccount("Dharani", 1000)
savings = SavingsAccount("Dharani", 1000)
savings.deposit(500)
savings.withdraw(300)
savings.withdraw(1500)
savings.add_interest()

