def canConstruct(ransomNote, magazine):
        ransomCnt = collections.Counter(ransomNote)  # ransomNote中各个字符的个数
        magazineCnt = collections.Counter(magazine)  # magazine中各个字符的个数
        return not ransomCnt - magazineCnt           # 如果ransomCnt中字符个数大于magazineCnt，返回False
