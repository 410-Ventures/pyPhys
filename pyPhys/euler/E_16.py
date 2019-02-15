
"""
Andrew Kavas
Power Digit Sum

"""

def int_sum(var):
    sep = [int(i) for i in str(var)]
    print(sep)
    sumnum = 0
    for kk in range(0,len(sep)):
        sumnum += sep[kk]
    print(sumnum)

int_sum(2**1000)
