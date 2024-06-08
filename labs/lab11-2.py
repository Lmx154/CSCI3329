def calculate_area(x1, y1, x2, y2, x3, y3):
    area = 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
    return area


points = input("Please input three points: ").split()
x1, y1, x2, y2, x3, y3 = map(int, points)
area = calculate_area(x1, y1, x2, y2, x3, y3)
print("The area is", int(area))
