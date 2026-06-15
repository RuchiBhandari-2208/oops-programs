class calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b

cal = calculator()

print(cal.add(10, 5))
print(cal.subtract(10, 5))
print(cal.multiply(10, 5))
print(cal.divide(10, 5))