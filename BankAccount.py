class BankAccount:
    def __init__(self):
        self.balance = 0
 
    def deposit(self, amount):
        self.balance += amount
 
    def withdraw(self, amount):
        self.balance -= amount
 
    def check_balance(self):
        print("Balance:", self.balance)
 
 
acc = BankAccount()
 
acc.deposit(5000)
acc.withdraw(1000)
 
acc.check_balance()