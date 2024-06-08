
x1, y1 = input("Enter the x and y coordinates of the first point: ").split()

x2, y2 = input("Enter the x and y coordinates of the second point: ").split()

distance_squared = (int(x2) - int(x1))**2 + (int(y2) - int(y1))**2

print(int(distance_squared**0.5))
