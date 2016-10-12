'''
 Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

'''

# 一开始的想法是用s.index(i)返回index的，但是时间超了


import collections
def firstUniqChar(s):
    result = -1
    char_s = collections.Counter(s)       # 取得每个字符的个数
    for i, c in enumerate(s):       
        if char_s[c] == 1:                # 在s中取得个数为1的char
            result = i                    # 返回index
            break
    return result
