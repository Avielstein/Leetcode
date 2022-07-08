class Solution(object):
    def maxProfit(self, p):
        max_profit, min_price = 0, float('inf')
        for i in p:
            min_price = min(min_price, i)
            profit = i - min_price
            max_profit = max(max_profit, profit)
        return max_profit

        