'''
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
'''


def convertToTitle(n):
    remainder = []
    while n > 26:        
        if n % 26 == 0:                          # 遇到余数为0的特殊情况，例如52/26=2, 52%26=0 
            remainder.append((n % 26)+26)        # 商要减1，余数加上26
            n =n / 26 -1
        else:
            remainder.append(n % 26)             # 正常情况直接按进制转换
            n = n / 26
    remainder.append(n)
    remainder.reverse()
    result = ''
    for i in remainder:
        result += chr(ord('A')+i-1)              
    return result
