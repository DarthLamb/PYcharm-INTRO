class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self, mileage):
        """Set odometer with the given value
        Reject the change if it attempts to roll the odometer back"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back the odometer!")

    def increment_odometer(self, miles):
        """Add a given amount to the odometer reading"""
        self.odometer_reading += miles

# my_new_car = Car('audi', 'a4', 2019)
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()
#
# """Modifying an attributes value directly"""
# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()
# """Modifying an attribute through a method""" b vvvv  b
# my_new_car.update_odometer(26)
# my_new_car.read_odometer()
# my_new_car.update_odometer(22)
# """Incrementing an attribute value through a method"""
# my_second_car = Car('subaru', 'outback', 2020)
# print(my_second_car.get_descriptive_name())#"""Get descriptive name is pretty important function"""
# my_second_car.update_odometer(20_324)
# my_second_car.read_odometer()
# my_second_car.increment_odometer(100)
# my_second_car.read_odometer()

