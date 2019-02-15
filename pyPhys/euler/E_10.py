
"""
Andrew Kavas
E_10
Primes Sum

"""

from primes_sieve import primes_sieve1

def prime_sum(limit):
    barr = primes_sieve1(limit)
    count = 0
    for kk in range(0,len(barr)):
        count += int(barr[kk])
    print(count)
    
#    for kk in range(0,len(barr)):
#        arr.append(barr)


prime_sum(2000000)

#12272557818053
#12272577818052