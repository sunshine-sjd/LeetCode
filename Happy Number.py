'''
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

    12 + 92 = 82
    82 + 22 = 68
    62 + 82 = 100
    12 + 02 + 02 = 1
'''

def isHappy(n):
    visited_nums = []
    while n != 1 and n not in visited_nums:   # 循环的停止条件是n=1位happy number或者是n经过几次计算后的sum在visited_num再次出现
        visited_nums.append(n)
        digits = map(int, str(n))
        n = sum(d**2 for d in digits)
    return n == 1
