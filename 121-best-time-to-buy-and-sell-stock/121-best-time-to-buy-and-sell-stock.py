class Solution(object):
    def maxProfit(self, prices):
        max_profit, min_price = 0, float('inf')
        for p in prices:
            min_price = min(min_price, p)
            profit = p - min_price
            max_profit = max(max_profit, profit)
        return max_profit

        