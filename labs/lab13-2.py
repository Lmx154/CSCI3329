import numpy as np

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0/9.0

fahrenheit_values = np.array([32, 45, 50, 64, 72, 80, 90, 100, 110, 120])

celsius_values = fahrenheit_to_celsius(fahrenheit_values)

celsius_values_int = [int(value) for value in celsius_values]

print("Fahrenheit : ", fahrenheit_values)
print("Celsius : ", celsius_values_int)
