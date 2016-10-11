'''

Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 

'''





def titleToNumber(s):
    result = 0
    s_length = len(s)-1
    for s_str in s:
        result = result + 26 ** (s_length) * (ord(s_str)-ord('A')+1)   # 类似2进制转化为10进制，将26进制转化为10进制
        s_length -= 1
    return result
