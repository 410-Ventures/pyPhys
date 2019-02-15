
"""
Andrew Kavas
Local fun with Foobar

"""

for i in range(10):
    locals()['foobar{0}'.format(i)] = i * 3.14

print(foobar9)
