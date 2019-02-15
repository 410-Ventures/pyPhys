
"""
Andrew Kavas
1000 Digit Fibonacci Number

"""

def fib_len(num):
    a,b = 1,0
    for kk in range(1,num**2):
        b = a + b
        a = b - a
        print(kk,b)
        sep = [int(i) for i in str(b)]
        if len(sep) >= num:
            break
    print(b)
    return(kk)


print(fib_len(1000))


"""
c = a + b
a = b - a

"""
