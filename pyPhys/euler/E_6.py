
"""
Andrew Kavas
E_6
Square Diff

"""


def all_squared(num):
    count = 0
    for kk in range(1, num+1):
        count = count + kk**2
    return count


def sum_squared(num):
    ncount = 0
    for kk in range(1, num+1):
        ncount = ncount + kk
        print(ncount)
    ncount = ncount**2
    return ncount


def natch(num):
    diff = sum_squared(num) - all_squared(num)
    return diff


print(natch(100))

