    '''
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.

    '''
    
    
    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_Cnt = collections.Counter(s)      # 统计各个字符的出现的频率
        even_num = [i for i in s_Cnt.values() if i % 2 == 0] # 出现偶数次字符的各个对应个数
        odd_num = [i for i in s_Cnt.values() if i % 2 != 0]  # 出现奇数次字符的各个对应个数
        len_odd_num = len(odd_num) # 出现奇数次字符的个数
        if even_num == []:
            even_num = [0]
        if odd_num == []:      # 如果没有出现奇数或者偶数次的字符，对应的列表设置为0
            odd_num = [0]
        if len_odd_num == 0:
            result = sum(even_num) + sum(odd_num) - len_odd_num  # 出现偶数次的结果直接放入结果中，奇数次的字符减去1次也是偶数次，并加入
                                                                 # 结果中，最后加1，表示最长的那个奇数次字符可以放到回文的最中间，不用减1.
        else:
            result = sum(even_num) + sum(odd_num) - len_odd_num + 1
        return result    
        
