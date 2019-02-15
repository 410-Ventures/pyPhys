
"""
Andrew Kavas
fibs

"""


def fib(num):
    a, b = 1, 0
    arr = []
    arr.append(0)
    for kk in range(0, num):
        b = a + b
        a = b - a
        arr.append(b)
    print(arr)
    return arr[-1]


def limit(value):
    for kk in range(0, value):
        if fib(kk) < value:
            kk = kk + 1
        else:
            break
    print(fib(kk - 1))
    print(sum_even(kk))


def sum_even(fib_num):
    evens = 0
    for jj in range(0, fib_num):
        if fib(jj) % 2 == 0:
            evens = evens + fib(jj)
        else:
            evens += 0
    return evens


limit(4000000)


"""

a = second to last element
b = current element
c = next element

c = a + b
a = b

"""
