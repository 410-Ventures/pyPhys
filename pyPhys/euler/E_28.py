
"""
Andrew Kavas
E_28
Spiral Matrix

"""


def spiral(num):
    count = 1
    kk = 3
    while kk < num+1:
        count += kk**2 + kk**2-(kk-1) + kk**2 - 2*(kk-1) + kk**2 - 3*(kk-1)
        kk += 2
        print(count)

spiral(1001)


