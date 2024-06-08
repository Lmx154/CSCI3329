a, b, c, d = input("Input: ").split()

a, b, c, d = int(a), int(b), int(c), int(d)


if (a == b and c == d) or (a == c and b == d) or (a == d and b == c):
    print("Output: YES")
else:
    print("Output: NO")
