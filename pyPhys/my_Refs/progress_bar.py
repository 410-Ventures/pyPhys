
"""
Andrew Kavas


"""

import sys

# Works best for iterations of less than 100,000
# I'm working on a more succinct code that updates less often
# update_progress() : Displays or updates a console progress bar
# Accepts a float between 0 and 1. Any int will be converted to a float.
# A value under 0 represents a 'halt'.
# A value at 1 or bigger represents 100%

def updt(total, progress):
    """
    Displays or updates a console progress bar.

    Original source: https://stackoverflow.com/a/15860757/1391441
    """
    
    barLength, status = 20, ""
    progress = float(progress) / float(total)
    if progress >= 1.:
        progress, status = 1, "\r\n"
    block = int(round(barLength * progress))
    text = "\r[{}] {:.0f}% {}".format(
        "#" * block + "-" * (barLength - block), round(progress * 100, 0),
        status)
    sys.stdout.write(text)
    sys.stdout.flush()


#PRIME EXAMPLE:
#def primes_sieve1(limit):
#    limitn = limit+1
#    primes = dict()
#    for i in range(2, limitn): primes[i] = True
#    for i in primes:
#        factors = range(i,limitn, i)
#        
#        updt(limit, i)
#        
#        for f in factors[1:]:
#            primes[f] = False
#    return [i for i in primes if primes[i]==True]
#
#print(primes_sieve1(2000))
