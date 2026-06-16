class Movie:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating
 
    def display(self):
        print("Movie:", self.name)
        print("Rating:", self.rating)
 
 
m = Movie("Pushpa", 8.2)
 
m.display()