'''
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, 
the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
'''
'''
动态规划
复杂度

时间 O(N) 空间 O(1)
思路

一般来说，给定一个规则，让我们求任意状态下的解，都是用动态规划。这里的规则是劫匪不能同时抢劫相邻的屋子，即我们在累加时，只有两种选择：

    如果选择了抢劫上一个屋子，那么就不能抢劫当前的屋子，所以最大收益就是抢劫上一个屋子的收益

    如果选择抢劫当前屋子，就不能抢劫上一个屋子，所以最大收益是到上一个屋子的上一个屋子为止的最大收益，加上当前屋子里有的钱

所以，我们只要判断一下两个里面哪个大就行了，同时也是我们的递推式。另外我们可以做一点优化，本来我们是要用一个dp数组来保存之前的结果的。但实际上我们只需要上一次和上上次的结果，所以可以用两个变量就行了。
'''

# 动态规划   知乎概念解释 https://www.zhihu.com/question/23995189

def rob(nums):
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, len(nums)):
        dp[i] = max(dp[i-1], dp[i-2]+nums[i])
    return dp[-1]
