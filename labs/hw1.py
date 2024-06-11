def do_intersect(p1, q1, p2, q2):# Check if points intersect
    def ccw(A, B, C):# Check orientation of points
        return (C[1] - A[1]) * (B[0] - A[0]) > (B[1] - A[1]) * (C[0] - A[0])

    return ccw(p1, p2, q2) != ccw(q1, p2, q2) and ccw(p1, q1, p2) != ccw(p1, q1, q2)

# Read input from file
file = open('input.txt', 'r')
data = file.readlines()
file.close()

num_tests = int(data[0].split()[0])
results = []

# Process each test case
for i in range(1, num_tests + 1):
    values = [int(value) for value in data[i].split()]
    x1, y1, x2, y2, x3, y3, x4, y4 = values
    p1, q1, p2, q2 = (x1, y1), (x2, y2), (x3, y3), (x4, y4)
    if do_intersect(p1, q1, p2, q2):
        results.append('1')
    else:
        results.append('0')

# Write results to output file
file = open('output.txt', 'w')
for result in results:
    file.write(result + '\n')
file.close()

print("Results have been written to output.txt")
