n1, n2, n3 = input("Please enter 3 numbers: ").split()

n1, n2, n3 = int(n1), int(n2), int(n3)

max_val, min_val = 0, 0

if n1 > n2 and n1 > n3:
    max_val = n1
elif n2 > n1 and n2 > n3:
    max_val = n2
else:
    max_val = n3

if n1 < n2 and n1 < n3:
    min_val = n1
elif n2 < n1 and n2 < n3:
    min_val = n2
else:
    min_val = n3

print("Maximum is", max_val)
print("Minimum is", min_val)
