class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        hold,pre_hold,sell,pre_sell=-2**31,0,0,0
        for price in prices:
            pre_hold=hold
            hold=max(pre_hold,pre_sell-price)
            pre_sell=sell
            sell=max(pre_sell,pre_hold+price)
        return sell
        
        