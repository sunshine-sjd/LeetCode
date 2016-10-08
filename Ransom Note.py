def canConstruct(ransomNote, magazine):
        ransomCnt = collections.Counter(ransomNote)  # ransomNote中各个字符的个数
        magazineCnt = collections.Counter(magazine)  # magazine中各个字符的个数
        return not ransomCnt - magazineCnt           # 如果ransomCnt中字符个数大于magazineCnt，返回False




'''
关于collections.Counter的使用方法：

In:
import collections
a1 = collections.Counter('absnsms')
a2 = collections.Counter('rtgss')
print a1
print a2
print a1 - a2

Out:
Counter({'s': 3, 'a': 1, 'b': 1, 'm': 1, 'n': 1})
Counter({'s': 2, 'r': 1, 't': 1, 'g': 1})
Counter({'a': 1, 's': 1, 'b': 1, 'm': 1, 'n': 1})

'''
