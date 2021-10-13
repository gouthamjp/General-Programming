# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        maxp = 0
        
        while r<len(prices):
            if prices[l] < prices[r]:
                temp = prices[r] - prices[l]
                maxp = max(temp,maxp)
            else:
                l = r
            r += 1
        return maxp