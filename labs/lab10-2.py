k = int(input("Please input K: "))
while k < 0:
    print("Please input a positive number")
    k = int(input("Please input K: "))

primes = []
num = 2

while len(primes) < k:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)
    num += 1

print("Prime numbers:", *primes)
