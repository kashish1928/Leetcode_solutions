class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        left = 0
        right = 1
        if(len(prices) == 1):
            return 0
        while(right < len(prices)): 
            if(prices[right]-prices[left] < max_profit):
                if(prices[right] < prices[left]):
                    left = right
            else:
                max_profit = prices[right]-prices[left]
            right+=1
        return max_profit