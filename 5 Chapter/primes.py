
def genPrimes():

    primes = [2,3]
    yield 2
    yield 3
    prime_next = 3
    while True:

        prime_next += 1
        check = 0
        for prime in primes:
            if prime_next % prime !=0:
                check += 1

        if len(primes) == check:
            primes.append(prime_next)
            yield prime_next




foo = genPrimes()

for i in range(0,100):
    print(foo.__next__())
