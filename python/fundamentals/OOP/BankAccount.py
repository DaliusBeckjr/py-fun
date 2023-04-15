class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
        self.interest = int_rate
        self.balance = balance


    def deposit(self, amount):
        #deposit(self, amount) - increases the account balance by the given amount
        # your code here
        self.balance += amount
        print(f'Your balance is: {self.balance}')
        return self

    def withdraw(self, amount):
        # your code here
        # self.balance -= amount
        # print(f'Your balance is: {self.balance}')
        if amount < self.balance:
            self.balance -= amount
            print(f'Your balance is: {self.balance}')
        else:
            print("insufficient funds")
        return self
        


    def display_account_info(self):
        # your code here
        print(f'Your balance is: {self.balance}')
        return self

    def yield_interest(self):
        # your code here
        self.balance = (self.interest * self.balance) + self.balance
        print(f'Your balance is: {self.balance}')
        return self

# bonus: use a classmethod to print all instances of a Bank Account's info




user_1 = BankAccount(0.035, 500)
# make 3 deposits and 1 withdrawal, then yield interest and display 
# the account's info all in one line of code (i.e. chaining)
user_1.display_account_info().deposit(3000).deposit(50).deposit(100).withdraw(20).yield_interest()

user_2 = BankAccount(0.04, 500)
# 2 deposits and 4 withdrawals, then yield interest and display 
# the account's info all in one line of code
user_2.display_account_info().deposit(500).deposit(240).withdraw(50).withdraw(100).withdraw(30).withdraw(20).yield_interest()








