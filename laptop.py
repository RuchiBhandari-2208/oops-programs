class Laptop:
    def __init__(self, brand, processor, price):
        self.brand = brand
        self.processor = processor
        self.price = price

    def display(self):
        print(self.brand)
        print(self.processor)
        print(self.price)

l = Laptop("Dell", "i7", 70000)
l.display()