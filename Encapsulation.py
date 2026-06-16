class Account:
 
    def __init__(self):
        self.__balance = 0
 
    def deposit(self, amount):
        self.__balance += amount
 
    def show_balance(self):
        print("Balance:", self.__balance)
 
 
a = Account()
 
a.deposit(5000)
 
a.show_balance()