
def calculate_rectangle_area(circles):
    leftmost = float('inf')
    rightmost = float('-inf')
    topmost = float('-inf')
    bottommost = float('inf')

    for circle in circles:
        x, y, r = circle
        leftmost = min(leftmost, x - r)
        rightmost = max(rightmost, x + r)
        bottommost = min(bottommost, y - r)
        topmost = max(topmost, y + r)

    width = rightmost - leftmost
    height = topmost - bottommost
    area = width * height
    return area


M = int(input())
circles = []
for i in range(M):
    x, y, r = input().split()
    x, y, r = float(x), float(y), float(r)
    circles.append((x, y, r))

area = calculate_rectangle_area(circles)
print(f"{area:.2f}")
