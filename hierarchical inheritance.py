class Shape:
 
    def message(self):
        print("Shape Class")
 
 
class Rectangle(Shape):
    pass
 
 
class Circle(Shape):
    pass
 
 
r = Rectangle()
c = Circle()
 
r.message()
c.message()