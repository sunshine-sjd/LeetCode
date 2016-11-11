'''
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.
'''

def plusOne(digits):
    flag = 0
    len_digits = len(digits)
    for i in range(len_digits-1, -1, -1):
        if (digits[i] + 1) / 10 == 0:
            digits[i] += 1
            flag = 0
            break
        else:
            digits[i] = (digits[i]+1) % 10
            flag = 1
    if flag == 1:
        digits.insert(0, 1)
    return digits
