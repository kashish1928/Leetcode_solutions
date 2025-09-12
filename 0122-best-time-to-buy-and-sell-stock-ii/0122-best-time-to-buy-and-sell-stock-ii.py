class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        buy = 0
        for i in range(1,len(prices)):
            if(prices[buy] > prices[i] or prices[i-1]>prices[i]):
                profit+=(prices[i-1]-prices[buy])
                buy=i
        return profit + (prices[-1]-prices[buy])
        
        