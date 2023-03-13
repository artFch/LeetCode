class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        buy = 0
        sell = 1
        maximum = 0
        while sell < n:
            profit = prices[sell] - prices[buy]
            if prices[buy] < prices[sell]:
                maximum = max(profit, maximum)
            else:
                buy = sell
            sell += 1
        return maximum
