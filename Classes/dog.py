class Dog:
    """The creation of the Dog Class"""
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate a dog rolling over"""
        print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 9)
your_dog = Dog('Lucy', 10)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
print(f"My dog's name is {your_dog.name}.")
print(f"My dog is {your_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()
your_dog.sit()
your_dog.roll_over()
