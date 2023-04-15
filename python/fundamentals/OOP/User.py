class User:

    def __init__(self, first_name, last_name, email, age):


        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        # setting attributes
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(f" First name: {self.first_name} \n Last name: {self.last_name}")
        print(f" Email: {self.email} \n Age: {self.age}")

    def enroll(self):
        self.is_rewards_member = True





john = User("john", "kennedy", "john@email.com", 34)
john.display_info()


