
#Andrew Kavas
#Smallest Multiple


def small_mult():
    kk = 1000000
    while any([kk%20 !=0,kk%19 !=0,kk%18 !=0,kk%17 !=0,kk%16 !=0,kk%15 !=0,kk%14 !=0,kk%13 !=0,kk%12 !=0,kk%11 !=0,kk%10 !=0,kk%9 !=0,kk%8 !=0]):
        kk += 20
    print(kk)


small_mult()
