
"""
Andrew Kavas
Smallest integer divisible by 0->n
E_5 (improved)

"""

from math import log
import prime_sieve

def prime_sieve(n):
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return([2] + [2*i+1 for i in range(1,n//2) if sieve[i]])

L = int(input('Smallest number evenly divisible by all int from 1->'))
primes = prime_sieve(L+1)

a = 1
for p in primes:
    a*= p**int(log(L)/log(p))
    
print("is", a)

