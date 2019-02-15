
"""
Andrew Kavas
Fibonacci

"""

def fib(num):
    a, b = 1,0
    arr = []
    arr.append(0)
    for kk in range(0,num):
        b = a + b
        a = b - a
        arr.append(b)
    print(arr)
    return(arr[-1])
    
fib(10)
