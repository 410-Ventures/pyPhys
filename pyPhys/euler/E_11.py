
"""
Andrew Kavas
Largest Product in a Grid
E_11

** Needs matrix file from Euler saved as E_11_matrix.txt **

"""

import numpy as np

arr = []
varr = []
rarr = np.zeros((20,20))

with open('E_11_matrix.txt', 'r') as f:
    for line in f:
        arr.append(line)
        split_line = line.split(' ')
        #varr.append(split_line)
        for values in split_line:
                value_as_int = int(values)
                varr.append(value_as_int)

for kk in range(0,20):
    rarr[kk] = varr[kk*20:(kk+1)*20]

print('//')

#print(arr)
#print(varr)
#print(rarr)
#print(rarr[1,0])

prods = []

def sweep(num):
    for jj in range(0,20):
        for kk in range(0,17):
            prod = rarr[jj,kk]*rarr[jj,kk+1]*rarr[jj,kk+2]*rarr[jj,kk+3]
            prods.append(prod)
#            #print(prod)
    for jj in range(0,20):
        for kk in range(0,17):
            prod = rarr[kk,jj]*rarr[kk+1,jj]*rarr[kk+2,jj]*rarr[kk+3,jj]
            prods.append(prod)
#            #print(prod)
    for jj in range(0,17):
        for kk in range(0,17):
            prod = rarr[kk,jj]*rarr[kk+1,jj+1]*rarr[kk+2,jj+2]*rarr[kk+3,jj+3]
            prods.append(prod)
#            #print(prod)
    for jj in range(0,17):
        for kk in range(0,17):
            prod = rarr[kk+3,jj]*rarr[kk+2,jj+1]*rarr[kk+1,jj+2]*rarr[kk,jj+3]
            prods.append(prod)
            #print(prods)
    print(prods)
    print('//')
    print(max(prods))

sweep(4)
            

#print(prods)
#print(len(prods))

