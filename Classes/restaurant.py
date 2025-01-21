class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
         print(f"{self.restaurant_name} tastes very good! Their cuisine is", self.cuisine_type)

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

restaurant_one = Restaurant("Mikey's", 'American')
restaurant_two = Restaurant("Donald's", "Thai")
restaurant_three = Restaurant("Rick's", "Chinese")

print(f"I love to go to {restaurant_one.restaurant_name} on Fridays!")
print(f"They have the best {restaurant_one.cuisine_type} food in town!")

restaurant_one.describe_restaurant()
restaurant_two.describe_restaurant()
restaurant_three.describe_restaurant()

