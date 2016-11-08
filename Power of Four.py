'''
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example:
Given num = 16, return true. Given num = 5, return false.

Follow up: Could you solve it without loops/recursion? 
'''


def isPowerOfFour(num):
    from math import log
    log_of_num = log(num, 4)
    print(log_of_num)
    return int(log_of_num) == log_of_num
