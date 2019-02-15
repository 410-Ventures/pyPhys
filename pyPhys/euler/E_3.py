#Andrew Kavas
#Primes


from sympy.ntheory.generate import primerange


def high_prime(var):

    primes = list(primerange(2, int(var**.5)+1))
    prime_list = []
    
    for kk in range(0, len(primes)):
        if var % primes[kk] == 0:
            prime_list.append(primes[kk])
    print(prime_list)

    for jj in range(len(prime_list)-1, 0, -1):
        while prime_list[jj] % prime_list[0] == 0:
            prime_list.remove(prime_list[jj])
            jj = jj - 1
        else:
            break
    return prime_list[-1]


def main():
    num = int(input('Type your number my person: '))
    print(high_prime(num))


print(main())
