
class User:


    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    # other methods
    # Add a make_deposit method to the User class that calls on it's bank account's instance methods.
    def make_deposit(self, amount):
    # your code here
        # self.account += amount
        self.account.deposit(amount)
        print(f"your balance is: {self.account.balance}")
        return self

    # Add a make_withdrawal method to the User class that calls on it's bank account's instance methods.
    def make_withdraw(self, amount):
    # your code here
        # self.balance -= amount 
        self.account.withdraw(amount)
        print(f"your balance is: {self.account.balance}")
        return self

    def make_yield(self):
        self.account.yield_interest()

    # Add a display_user_balance method to the User class that displays user's account balance
    # maybe turn into a @classmethod
    def display_user_balance(self):
    # your code here
        # print(f"{self.name} balance is: ")
        print(f"name : {self.name}")
        print(f"email: {self.email}")
        self.account.display_account_info()
        return self


class BankAccount:
    def __init__(self, int_rate=0.02, balance=0):
        self.interest = int_rate
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        # print(f"Your balance is {self.balance}")
        return self

    def withdraw(self,amount):
        self.balance -= amount
        # print(f"Your balance is {self.balance}")
        # if amount < self.balance:
        #     self.balance -= amount
        #     print(f'Your balance is: {self.balance}')
        # else:
        #     print("insufficient funds")
        return self

    def display_account_info(self):
        print(f"-------")
        print(f"your balance is: {self.balance}")

    def yield_interest(self):
        # your code here
        if self.balance > 0:
            self.balance = (self.interest * self.balance) + self.balance
            print(f'Your balance is: {self.balance}')
        return self



user_1 = User("john", "john@email.zom")
user_1.display_user_balance().make_deposit(30).make_withdraw(50).make_yield()
# user_1.deposit(30).deposit(100).withdraw(80).display_user_balance()
# jacob = User("jacob", "johnson", 38)
# donny = User("donny", "king", 43)