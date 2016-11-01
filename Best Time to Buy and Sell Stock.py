'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:

Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)

Example 2:

Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.


'''

def maxProfit(prices):
    if len(prices) <= 1:
        return 0
    low_price = prices[0]
    maxprofit = 0
    len_prices = len(prices)
    for i in range(len_prices):
        if prices[i] < low_price:
            low_price = prices[i]
        maxprofit = max(maxprofit, prices[i]-low_price)
    return maxprofit
