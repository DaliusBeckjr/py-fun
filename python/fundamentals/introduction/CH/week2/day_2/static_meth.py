

class User:

    all_users =[]
    
    def __init__(self, f_name, l_name, age):
        self.first_name = f_name
        self.last_name = l_name
        self.age = age
        # we are taking the creation of self and appending it to the all_users
        # attribute
        User.all_users.append(self)

    def change_first_name(self, new_name):
        self.first_name = new_name
        return self # needed to chain methods

    def birthday(self):
        self.age += 1
        print(f"Happy birthday you're older")
        return self 

    # if you want to display all the instances, then use a classmethod and 
    # access the class attribute
    @classmethod
    def display_all_users(cls):
        # pass
        print(cls.all_users)
        # without cls it would think all_users is a variable that is not defined yet
        for user in cls.all_users:
            print(user.first_name)

john = User("john", "wallace", 27)
jacob = User("jacob", "johnson", 38)
donny = User("donny", "king", 43)

# invoke a method
User.display_all_users()

john.change_first_name("joseph").birthday()