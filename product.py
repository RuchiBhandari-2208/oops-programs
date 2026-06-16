class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
 
    def total_cost(self):
        return self.price * self.quantity
 
 
p = Product("Mouse", 500, 3)
 
print("Total Cost:", p.total_cost())