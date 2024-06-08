import math

x, y = input().split()

r = float(input())

x1, y1, x2, y2 = input().split()
x, y, x1, y1, x2, y2 = float(x), float(y), float(x1), float(y1), float(x2), float(y2)

d = abs((y2 - y1) * x - (x2 - x1) * y + x2 * y1 - y2 * x1) / math.sqrt((y2 - y1)**2 + (x2 - x1)**2)

if d >= r:
    area = math.pi * r**2
else:
    theta = 2 * math.acos(d / r)
    segment_area = (r**2 / 2) * (theta - math.sin(theta))
    area = math.pi * r**2 - segment_area

print(area)
