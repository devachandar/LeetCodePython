class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp = prices[0]
        max_profit = 0
        profit_sum = 0

        for i in range(1,len(prices)):
            if prices[i] < prices[i-1]:
                mp = prices[i]
                profit_sum = profit_sum + max_profit
                max_profit = 0

            
            max_profit = max(max_profit,prices[i] - mp)
        
        profit_sum = profit_sum + max_profit

        return profit_sum