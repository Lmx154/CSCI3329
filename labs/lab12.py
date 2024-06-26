class Car:
    def __init__(self, brand, model, year):  # declare brand, model, and year as parameters for the __init__ method
        self.brand = brand  # initialize the brand attribute with the brand parameter
        self.model = model  # initialize the model attribute with the model parameter
        self.year = year    # initialize the year attribute with the year parameter


# Minivan class inherits from Car class
class Minivan(Car):
    def __init__(self, brand, model, year, hasASD):  # declare brand, model, year, and hasASD as parameters for the __init__ method
        super().__init__(brand, model, year)  # call the __init__ method of the superclass Car to initialize brand, model, and year
        self.hasASD = hasASD  # initialize the hasASD attribute specific to the Minivan class


# Create an instance of Minivan
m1 = Minivan("Toyota", "Sienna", "2023", True)
# Create an instance of Car
c1 = Car("Toyota", "Camry", "2024")

# Print attributes of the Minivan instance
print(m1.brand, m1.model, m1.year)  # Output: Toyota Sienna 2023
# Print attributes of the Car instance
print(c1.brand, c1.model, c1.year)  # Output: Toyota Camry 2024
