class Grandfather:
    def house(self):
        print("House")
 
 
class Father(Grandfather):
    def car(self):
        print("Car")
 
 
class Son(Father):
    def bike(self):
        print("Bike")
 
 
s = Son()
 
s.house()
s.car()
s.bike()