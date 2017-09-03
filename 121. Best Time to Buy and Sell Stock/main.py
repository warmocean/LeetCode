class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_dif = 0
        if len(prices) > 1: 
            min_idx = 0
            for i in range(len(prices)):
                if prices[i] < prices[min_idx]:
                    min_idx = i
                if max_dif < prices[i] - prices[min_idx]:
                    max_dif = prices[i] - prices[min_idx]
                    
       '''
        max_profit, min_price = 0, float('inf')
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
        ''' 
                
        return max_dif
