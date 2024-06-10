def find_min_rectangle_area(circles):
    min_x = float('inf')
    min_y = float('inf')
    max_x = float('-inf')
    max_y = float('-inf')

    for circle in circles:
        cx, cy, r = circle
        min_x = min(min_x, cx - r)
        min_y = min(min_y, cy - r)
        max_x = max(max_x, cx + r)
        max_y = max(max_y, cy + r)

    width = max_x - min_x
    height = max_y - min_y
    area = width * height

    return area

M = int(input("Input: "))
circles = []

for i in range(M):
    c1x, c1y, c1r = [float(i) for i in input().split()]
    circles.append((c1x, c1y, c1r))

area = find_min_rectangle_area(circles)
print(f"Output: {area:.2f}")
