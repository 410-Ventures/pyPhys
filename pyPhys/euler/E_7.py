
"""
Andrew Kavas
Easy Primes
"""

from sympy.ntheory.generate import prime

def easy_prime(var):
    print(prime(var))

easy_prime(10001)

# def sieve_algg():
#
#     n = 10**6
#
# # try set
#
#     num = set(range(2,n))
#
# # and compare how Sieve algorithm scales against array
#
#     arr = np.arange(2,n)
#
#     tick = time.time()
#
#     tock = time.time()
#
#     time_delta = float(tock - tick)
#
#     fin =
#
#     print("It took us exactly T ={} s to generate {} prime \
#     numbers ".format(time_delta,n))
#
#     print(fin[-1])
