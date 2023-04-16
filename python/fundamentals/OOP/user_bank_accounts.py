
class User:


    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    # other methods
    # Add a make_deposit method to the User class that calls on it's bank account's instance methods.
    def make_deposit(self, amount):
    # your code here
        self.account += amount
        self.account.deposit(amount)
        return self

    # Add a make_withdrawal method to the User class that calls on it's bank account's instance methods.
    def make_withdraw(self, amount):
    # your code here
        self.balance -= amount 
        self.account.withdraw(amount)
        return self

    # Add a display_user_balance method to the User class that displays user's account balance
    # maybe turn into a @classmethod
    def display_user_balance(self):
    # your code here
        print(f"{self.name} balance is: ")
        self.account.display_account_info()
        return self


class BankAccount:
    def __init__(self, int_rate=0.02, balance=0):
        self.interest = int_rate
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self,amount):
        self.balance -= amount
        return self



user_1 = User("john", "john@email.zom")
user_1.make_deposit(30).make_withdraw(100).display_user_balance()
# user_1.deposit(30).deposit(100).withdraw(80).display_user_balance()
# jacob = User("jacob", "johnson", 38)
# donny = User("donny", "king", 43)