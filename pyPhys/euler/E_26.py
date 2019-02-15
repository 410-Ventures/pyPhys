
"""
Andrew Kavas
E_26
Reciprocal Cycles

"""

from Euler import prime_sieve

def f(N):
    if N < 8: return 3
    for d in prime_sieve(N)[::-1]:
        period = 1
        while pow(10, period) % d != 1: period += 1
        if d-1 == period: return d

N = 1000
print("is d =", f(N))


