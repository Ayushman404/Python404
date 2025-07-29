#Add a class variable to Car that keeps track of the number of cars created

class Car:
    
    total_car = 0
    
    # constrctor
    def __init__ (self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_car += 1
        
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

my_car = Car("Porsche", "Corolla")

print(Car.total_car)    

