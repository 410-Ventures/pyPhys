
"""
Andrew Kavas
Prime Sieve
Sieve of Eratosthenes

"""

import time


def primes_sieve1(limit):
    limitn = limit+1
    primes = dict()
    for i in range(2, limitn): primes[i] = True

    for i in primes:
        factors = range(i,limitn, i)
        for f in factors[1:]:
            primes[f] = False
    return [i for i in primes if primes[i]==True]


tick = time.time()
print(primes_sieve1(2000000))
tock = time.time()
print('Run time: ', tock-tick)

#18.3