# create an Electric Car class that inherits from the Car class and has an additional attribute battery_size
class Car:
    
    # constrctor
    def __init__ (self, brand, model):
        self.brand = brand
        self.model = model
        
    def full_name(self):
        return f"{self.brand} and {self.model}"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    
my_tesla = ElectricCar("Tesla", "Model S", "85kWh")

# print(my_tesla.model)
print(my_tesla.full_name())
print(my_tesla.battery_size)

my_car = Car("Porsche", "Corolla")
# print(my_car.brand)
# print(my_car.full_name())