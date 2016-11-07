'''
Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements equal, where a move is incrementing n - 1 elements by 1.

Example:

Input:
[1,2,3]

Output:
3

Explanation:
Only three moves are needed (remember each move increments two elements):

[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]

'''
# 排序后依次和最小的数相减，结果为各个差的和
def minMoves(nums):
    count = 0
    nums.sort()
    nums_len = len(nums)
    for i in range(1, nums_len):
        count += nums[i] - nums[0]
    return count
