class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        result = prices.copy()

        for i in range(len(prices)):

            while stack and prices[i] <= prices[stack[-1]]:
                idx = stack.pop()
                result[idx] = prices[idx] - prices[i]

            stack.append(i)

        # print(result)
        return result