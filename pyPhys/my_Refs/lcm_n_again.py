
"""
Andrew Kavas


"""

#
## Python program to find the smallest number evenly 
## divisible by all number 1 to n
#import fractions
# 
## Returns the lcm of first n numbers
#def lcm(n):
#    ans = 1   
#    for i in range(1, n + 1):
#        ans = (ans * i)/fractions.gcd(ans, i)        
#    return ans
# 
## main
#n = 50
#print(lcm(n))

def prime_sieve(n):
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return([2] + [2*i+1 for i in range(1,n//2) if sieve[i]])


print(prime_sieve(1998))
