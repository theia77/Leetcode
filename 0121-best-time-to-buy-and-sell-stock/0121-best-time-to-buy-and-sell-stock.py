class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_prices=prices[0]
        max_profit=0
        for i in range(len(prices)):
            if(min_prices>prices[i]):
                min_prices=prices[i]
            profit=prices[i]-min_prices
            if(profit>0):
                if(max_profit<profit):
                    max_profit=profit
        return max_profit
                

        
        

  