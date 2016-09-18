'''
Given a non-negative integernum, repeatedly add all its digits until the result has only one digit.
For example:
Givennum = 38, the process is like:3 + 8 = 11,1 + 1 = 2. Since2 has only one digit, return it.
Follow up:Could you do it without any loop/recursion in O(1) runtime?

结果发现其是以9为周期
'''

    def addDigits(num):
        if not num:
            return num
        res = num % 9
        return res if res else 9

