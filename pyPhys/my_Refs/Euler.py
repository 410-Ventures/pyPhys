
"""
Andrew Kavas
Prime Sieve of Eratosthenes

"""

#Generates list of prime numbers LESS than n in value
#Faster than siece of Atkin up to n = 10 billion


def prime_sieve(n):
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n//2) if sieve[i]]


#print(prime_sieve(1000000))

