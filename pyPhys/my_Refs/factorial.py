
"""
Andrew Kavas
Factorial

"""



def factorial(num):
    nxt = num - 1
    fact = num
    while nxt > 1:
        fact = fact*nxt
        nxt += -1
    print(fact)
    return(fact)

factorial(1000)
