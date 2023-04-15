# declare a class and give it name User
class User:


    # self is the instance of the class and can be used in all of our user methods
    def __init__(self, f_name, l_name, age):
        self.first_name = f_name
        self.last_name = l_name
        self.age = age
        # A method needs to be within the class 
        # underneath your constructor creating an unlimited amount of methods
    def greetings(self):
        print(f"hello my name is {self.first_name} {self.last_name}")
    
    def change_first_name(self, new_name):
        self.first_name = new_name
    
    def birthday(self):
        self.age += 1
        print(self.age)



# Now that you have a class set up with a constructor 
# You can assign new variables to new users in the outer scope!
# user_1 = User("john", "kennedy", 35)
# print(user_1.first_name) # prints john

# user_2 = User("sean", "wallace", 26)
# print(user_2.first_name) # prints sean

john = User("john", "kennedy", 35)
#print(john.first_name) # prints john
sean = User("sean", "wallace", 26)

john.greetings() # prints hello my name is john kennedy
john.change_first_name("joseph")
john.greetings() # prints hello my name is joseph kennedy
john.birthday()

# sean.greetings() # prints hello my name is sean wallace

