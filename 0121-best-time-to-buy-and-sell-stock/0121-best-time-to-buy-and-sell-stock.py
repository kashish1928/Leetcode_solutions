class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        left = 0
        right = 1
        best_day = 0
        if(len(prices) == 1):
            return 0
        while(right < len(prices)):
            profit = prices[right]-prices[left]
            if(profit < max_profit):
                if(prices[right] < prices[left]):
                    left = right
            else:
                max_profit = profit
                best_day = right
            right+=1
        return max_profit