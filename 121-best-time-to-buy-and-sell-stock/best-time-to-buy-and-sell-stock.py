class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        small = prices[0]
        profit = 0
        
        for i in range(1,len(prices)):
            profit = max(profit, prices[i] - small)

            if small > prices[i]:
                small = prices[i]

    
        return profit


        # profit = 0
        # min_prices = sys.maxsize
        # for i in range(len(prices)):
        #         if prices[i] < min_prices:
        #             min_prices = prices[i]
        #         profit = max(profit, prices[i] - min_prices)
        # return profit