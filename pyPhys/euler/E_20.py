
"""
Andrew Kavas
Factorial Int Sum

"""

def factorial(num):
    nxt = num - 1
    fact = num
    while nxt > 1:
        fact = fact*nxt
        nxt += -1
    return(fact)


def int_sum(var):
    sep = [int(i) for i in str(var)]
    print(sep)
    sumnum = 0
    for kk in range(0,len(sep)):
        sumnum += sep[kk]
    print(sumnum)


int_sum(factorial(100))


