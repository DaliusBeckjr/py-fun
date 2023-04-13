# For this assignment you will create the user class and add a couple methods!

class User:
    
    def __init__(self, f_name, l_name, age):
        user.first_name = f_name
        user.last_name = l_name
        user.age = age
        User.all_users.append(self)
    
    def change_name(self):
        pass

    # the 'all_user' without cls will be undf' 
    # cls is representing the 'user' class for cls.all_user
    @classmethod
    def display_all_users(cls):
        for user in cls.all_users:
            print(user)
            #print(user.first_name) # to print everyone first name


Donny = User('Donny', 'santos', 27)
Saint = User('Saint', 'Beck', 14)

User.display_all_users()

# think of staticmethod as a helper
