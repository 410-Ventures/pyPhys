#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 13:35:12 2018
@author: Andrew Kavas
"""

print("""
------------------------------------------------------
Andrew Kavas
1) Euler: 30
Digit Fifth Powers
------------------------------------------------------
""")

# Define functon in terms of power we are checking
# function should sum each digit to the power specified

def digits(power):
    nums = []
    # set range of numbers to evaluate
    for kk in range(2,10*10**power):
        # separate each number into array composed of each integer
        sep = str(kk)
        count = 0
        
        # for each element of array, raise each value to power
        # and add to count, which should clear for each new number
        for jj in range(0,len(sep)):
            count += int(sep[jj])**power
            
        # if sum of digits^power equals number, append number
        if count == kk:
            nums.append(count)
        else:
            continue
        
    # sum elements of array
    sum_num = 0
    for i in range(0,len(nums)):
        sum_num += nums[i]

    print(nums,sum_num)

digits(5)


