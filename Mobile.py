class Mobile:
    def __init__(self, company, ram, storage):
        self.company = company
        self.ram = ram
        self.storage = storage

    def display(self):
        print("Company:", self.company)
        print("RAM:", self.ram)
        print("Storage:", self.storage) 

m = Mobile("Samsung", "8GB", "128GB")
m.display()