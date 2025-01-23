class Restaurant:

    def __init__(self, restaurant_name, cuisine_type, number_served):

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
         print(f"{self.restaurant_name} tastes very good! Their cuisine is", self.cuisine_type)

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

    def update_num_served(self, people_served):
        self.number_served = people_served

    def increment_num_served(self, new_people_served):
        self.number_served += new_people_served

restaurant_one = Restaurant("Mikey's", 'American', 0)
restaurant_two = Restaurant("Donald's", "Thai", 10)
restaurant_three = Restaurant("Rick's", "Chinese", 20)

print(f"I love to go to {restaurant_one.restaurant_name} on Fridays!")
print(f"They have the best {restaurant_one.cuisine_type} food in town!")

restaurant_one.describe_restaurant()
restaurant_two.describe_restaurant()
restaurant_three.describe_restaurant()
print(restaurant_two.number_served)
restaurant_two.update_num_served(29)
print(restaurant_two.number_served)
restaurant_two.increment_num_served(20)
print(restaurant_two.number_served)
