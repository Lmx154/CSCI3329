x1, y1, x2, y2, x3, y3 = input("Please input 3 points: ").split()

x1, y1, x2, y2, x3, y3 = int(x1), int(y1), int(x2), int(y2), int(x3), int(y3)
area = 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))

print("The area is ", int(area))
