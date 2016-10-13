'''
Given two non-negative numbers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

    The length of both num1 and num2 is < 5100.
    Both num1 and num2 contains only digits 0-9.
    Both num1 and num2 does not contain any leading zero.
    You must not use any built-in BigInteger library or convert the inputs to integer directly.

'''


from itertools import izip_longest      # izip_longest类zip()，不过返回的是一个迭代器，不是列表，不够的位置可以用参数fillvalue设置填充
def addStrings(num1, num2):
    num1_num2_zip = izip_longest(num1[::-1], num2[::-1], fillvalue='0')  # 合并num1和num2，注意是反向的，方便从最低位开始相加
    carry = 0    # 进位
    result = ''
    for i, y in num1_num2_zip:
        s = int(i) + int(y) + carry     
        d = s % 10                  # i和y相加，并考虑有进位的情况
        carry = s / 10
        result += str(d)
    if carry > 0:                   # 最高位如果有进位则要加上去
        result += str(carry)
    return result[::-1]
