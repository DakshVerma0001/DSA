class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            if prices[i] < b:
                b = prices[i]
            
            profit = prices[i] - b

            if profit > max_profit:
                max_profit = profit
        
        return max_profit



        