'''
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.
'''

def trailingZeroes(n):
    res = 0
    while n >= 5 :
        res += n / 5
        n = n / 5
    return res
