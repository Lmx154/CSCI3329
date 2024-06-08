n = int(input("Please enter a number: "))

for i in range(n):
    for h in range(n - i - 1):
        print(" ", end="")
    for j in range(2 * i + 1):
        print("*", end="")
    print()
