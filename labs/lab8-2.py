g1, g2, g3 = input("Enter your grades (e.g., A B C): ").split()
total = 0.0

if g1 == 'A':
    total += 4.0
elif g1 == 'B':
    total += 3.0
elif g1 == 'C':
    total += 2.0

if g2 == 'A':
    total += 4.0
elif g2 == 'B':
    total += 3.0
elif g2 == 'C':
    total += 2.0

if g3 == 'A':
    total += 4.0
elif g3 == 'B':
    total += 3.0
elif g3 == 'C':
    total += 2.0

total = total/3

print("Your GPA is ", total)
