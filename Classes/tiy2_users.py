class User:
    def __init__(self, first_name, last_name, age, date_of_birth, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.date_of_birth = date_of_birth
        self.login_attempts = 0

    def describe_user(self):
        print(f"The user's name is: {self.first_name} {self.last_name}, age and date of birth:"
              f" {self.age}, {self.date_of_birth}, Login attempts:", self.login_attempts)
    def greet_user(self):
        print(f"Hello {self.first_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

first_user = User('Nick','Man', 10, '10/27/2003', 0)
second_user = User('Rick','Ban', 14, '09/27/2003', 0)
new_user = User('Bill', 'Nim', 12, '09/10/10',0 )


# first_user.describe_user()
# second_user.describe_user()
# first_user.greet_user()
# second_user.greet_user()
new_user.describe_user()
new_user.increment_login_attempts()
new_user.describe_user()
new_user.reset_login_attempts()
new_user.describe_user()
