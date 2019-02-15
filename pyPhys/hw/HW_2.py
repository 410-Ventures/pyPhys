#Andrew Kavas
#Multiples of 3 and 5

def mult(var):
	count = 0
	for i in range(1,var):
		if (float(i%5)==0 or float(i%3)==0):
			count += i
	return(count)
	
def main():
	varb = int(input('Sum of mult (3&5) up to n: '))
	print(mult(varb))
    
main()



#Andrew Kavas
#Primes

import numpy as np
from sympy.ntheory.generate import primerange

def high_prime(var):

    primes = list(primerange(2,int(var**.5)+1))
    prime_list = []
    
    for kk in range(0,len(primes)):
        if var % primes[kk] == 0:
            prime_list.append(primes[kk])
    print(prime_list)

    for jj in range(len(prime_list)-1,0,-1):
        while prime_list[jj] % prime_list[0] == 0:
            prime_list.remove(prime_list[jj])
            jj = jj-1
        else:
            break
    return(prime_list[-1])

def main():
    num = int(input('Highest prime factor below: '))
    print(high_prime(num))

print(main())




#Andrew Kavas
#Smallest Multiple

def small_mult():
    kk = 1000000
    while any([kk%20 !=0,kk%19 !=0,kk%18 !=0,kk%17 !=0,kk%16 !=0,kk%15 !=0,kk%14 !=0,kk%13 !=0,kk%12 !=0,kk%11 !=0,kk%10 !=0,kk%9 !=0,kk%8 !=0]):
        kk += 20
    print('Smallest number divisible by 1 -> 20 is: ', kk)

small_mult()




#Andrew Kavas
#Prime of N


import numpy as np
import time
from sympy.ntheory.generate import prime

def easy_prime(var):
    print('The 10001st prime is: ', prime(var))

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


#Andrew Kavas
#Pythagorean Triplets

def pythag():
    for a in range(1,1000):
        for b in range(a,1000):
            c = 1000-a-b
            if c > 0:
                if c**2 == a**2 + b**2:
                    print('Pythagorean triplet of c+a+b=1000 is: ', a, b, c, a*b*c)
                    break

pythag()


#Andrew Kavas
#Matrices and Vectors


import numpy as np

arr1 = np.matrix([[1,2,3],[11,22,33],[111,222,333]])
vec1 = np.matrix([[4],[5],[6]])

print('Matrix 1 (3x3): ',arr1)
print('Vector 1: ', vec1)

prod1 = arr1*vec1

print('Matrix Vector product: ', prod1)

arr3 = np.matrix([[1,1,1],[10,10,10],[100,100,100]])

print('Matrix 2 (3x3): ', arr3)

prod2 = arr1*arr3

print('Square Matrix Product: ', prod2)

arr4 = np.matrix([[1,1,1],[10,10,10],[100,100,100],[1000,1000,1000]])
arr5 = np.matrix([[2,3,4,5,6],[22,33,44,55,66],[222,333,444,555,666]])

print('Two matrices of different sizes', arr4,arr5)

prod3 = arr4*arr5

print('Product of KxL and LxM Matrix) ', prod3)


    
#Andrew Kavas
#Oscillators

    
import numpy as np
import matplotlib.pyplot as plt
from math import *

def oscillator( x = 0, v = 0.01, t = 0, tf = 20, steps = 100000):
#    v=0.01   #initial velocity
    dt=float((tf-t)/steps)
#    x=0.0   #initial position
#    t=0.0
    ta,xa=[],[]
    stepcount = 0
    while stepcount<steps:
        ta.append(t)
        xa.append(x)
        v=v-(10.0)*x*dt    #k=10.0, m=1.0
        x=x+v*dt
        t = t+dt
        stepcount+=1
    plt.figure()
    plt.plot(ta,xa,'g-')
    plt.xlabel('$t (s)$')
    plt.ylabel('$x (m)$')
    plt.show()
oscillator()

