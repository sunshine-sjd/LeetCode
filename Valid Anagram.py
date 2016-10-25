'''
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
'''

def isAnagram(s, t):
    s_counts = collections.Counter(s)
    t_counts = collections.Counter(t)
    return s_counts == t_counts
