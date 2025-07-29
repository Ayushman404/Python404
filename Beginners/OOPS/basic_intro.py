# Create a Car class with attribute like brand and model. Then create an instance of this class 

class Car:
    
    # constrctor
    def __init__ (self, brand, model):
        self.brand = brand
        self.model = model

my_car = Car("Porsche", "Corolla")
print(my_car.brand)
print(my_car.model)

my_new_car = Car("Tata", "Safari")
print(my_new_car.model)