from testField.prime import prime

n = 1
i = 1
primes = []
while i <= 500000:
    if prime(n):
        # print("!!", n, "!!")
        primes.append((i, n))
        i += 1
        if i % 15 == 0:
            print(*primes, sep=",")
            primes = []
    # else:
    #    print(n)
    if n > 2:
        n += 2
    else:
        n += 1
print(*primes, sep=", ")
