# Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar class, but with different behaviours 

class Car:
    
    # constrctor
    def __init__ (self, brand, model):
        self.__brand = brand
        self.model = model
        
    def get_brand(self):
        return self.__brand + "!"
        
    def full_name(self):
        return f"{self.__brand} and {self.model}"
    
    def fuel_type(self):
        return "Diseal or Petrol"



class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
    def fuel_type(self):
        return "Electricity"
    
    
my_tesla = ElectricCar("Tesla", "Model S", "85kWh")

print(my_tesla.get_brand())
print(my_tesla.fuel_type())

my_car = Car("Porsche", "Corolla")
print(my_car.fuel_type())

