n = int(input("Please enter a number: "))

for i in range(n):
    for h in range(i):
        print(" ", end="")
    for j in range(n - i):
        print("*", end="")
    print()
