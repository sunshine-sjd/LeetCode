'''
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

'''

def romanToInt(s):
    roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    position = 0
    length_s = len(s)
    result = 0
    while position < length_s - 1:
        if roman[s[position]] < roman[s[position+1]]:
            result -= roman[s[position]]
        else:
            result += roman[s[position]]
        position += 1
    result += roman[s[-1]]
    return result
