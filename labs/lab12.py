class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year


class Minivan(Car): # declare superclass is Car for inheritance
    def __init__(self, brand, model, year, hasASD): # child class method
        super().__init__(brand, model, year) # inheritance of method from superclass
        self.hasASD = hasASD # child class variable


m1 = Minivan("Toyota", "Sienna", "2023", True)
c1 = Car("Toyota", "Camry", "2024")


print(m1.brand, m1.model, m1.year)
print(c1.brand, c1.model, c1.year)
