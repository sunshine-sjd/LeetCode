def reverseVowels(s):
    total_vowels = 'AEIOUaeiou'  # 元音字母
    list_s = list(s)
    start = 0                   # 列表开头
    end = len(s)-1              # 列表末尾

    while start < end:          
        if list_s[start] not in total_vowels:    # 从列表首到尾，判断是否是元音字母，不是的index加1
            start += 1
        elif list_s[end] not in total_vowels:    # 从列表尾到首，判断是否是元音字母，不是的index减一
            end -= 1 
        else:                                    # 当两边都是元音字母时交换             
            list_s[start], list_s[end] = list_s[end], list_s[start]
            start += 1
            end -= 1
    return ''.join(list_s)
