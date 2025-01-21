class User:
    def __init__(self, first_name, last_name, age, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.date_of_birth = date_of_birth

    def describe_user(self):
        print(f"The user's name is: {self.first_name} {self.last_name}, age and date of birth:"
              f" {self.age}, {self.date_of_birth}")
    def greet_user(self):
        print(f"Hello {self.first_name}!")

first_user = User('Nick','Man', 10, '10/27/2003')
second_user = User('Rick','Ban', 14, '09/27/2003')

first_user.describe_user()
second_user.describe_user()
first_user.greet_user()
second_user.greet_user()

