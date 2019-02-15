
"""
Andrew Kavas
E_4
Palindromic Product

"""

def drome(num):
    arr = []
    for kk in range(1, num):
        for jj in range (1, num):
            a = str(kk*jj)
            b = a[::-1]
            if a == b:
                arr.append(a)
    arr = list(map(int, arr))
    print(max(arr))

drome(999)
