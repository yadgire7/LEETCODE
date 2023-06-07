'''
Approach: Sliding window
'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buy = prices[0]
        for p in prices:
            if p <= buy:
                buy = p
                continue
            profit = p - buy
            maxProfit = max(profit, maxProfit)
        return maxProfit
