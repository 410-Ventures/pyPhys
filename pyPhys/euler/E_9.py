#Andrew Kavas
#Pythagorean Triplets

def pythag():
    for a in range(1,1000):
        for b in range(a,1000):
            c = 1000-a-b
            if c > 0:
                if c**2 == a**2 + b**2:
                    print(a, b, c, a*b*c)
                    break

pythag()
