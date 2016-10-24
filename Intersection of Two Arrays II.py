'''
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:

    Each element in the result should appear as many times as it shows in both arrays.
    The result can be in any order.

Follow up:

    What if the given array is already sorted? How would you optimize your algorithm?
    What if nums1's size is small compared to nums2's size? Which algorithm is better?
    What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

'''

import collections
def intersect(nums1, nums2):
    intersect_nums = []
    for i in nums1:
        if i in nums2:     # 判断i是否也在nums2中
            intersect_nums.append(i)  # 把交集加入到intersect_nums
            nums2.remove(i)         # 删除nums2中已经判断出现过的元素，避免重复判断的额错误，例如  [1,1,2], [1,3]
    return intersect_nums
