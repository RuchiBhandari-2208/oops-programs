class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
 
    def display(self):
        print(self.brand)
        print(self.model)
        print(self.year)
 
 
car = Car("Toyota", "Fortuner", 2024)
 
car.display()