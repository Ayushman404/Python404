class Car:
    
    # constrctor
    def __init__ (self, brand, model):
        self.brand = brand
        self.model = model
        
    def full_name(self):
        return f"{self.brand} and {self.model}"

my_car = Car("Porsche", "Corolla")
# print(my_car.brand)
print(my_car.full_name())

# my_new_car = Car("Tata", "Safari")
# print(my_new_car.model)