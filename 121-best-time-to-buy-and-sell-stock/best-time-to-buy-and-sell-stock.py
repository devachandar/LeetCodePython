class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_prices = sys.maxsize
        for i in range(len(prices)):
                if prices[i] < min_prices:
                    min_prices = prices[i]
                profit = max(profit, prices[i] - min_prices)
        return profit