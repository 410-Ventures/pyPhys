
"""
Andrew Kavas


"""

x1 = float(input('x1 coord: '))
y1 = float(input('y1 coord: '))
z1 = float(input('z1 coord: '))

x2 = float(input('x2 coord: '))
y2 = float(input('y2 coord: '))
z2 = float(input('z2 coord: '))

def dist(x1,y1,z1,x2,y2,z2):
    """
    Enter float values only for coordinates
    Coooooooooooo
    """
    distance = ((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)**.5
    return distance

print('distance between points = ', dist(x1,y1,z1,x2,y2,z2))

