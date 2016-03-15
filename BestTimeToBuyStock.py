class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)==0:
            return 0
        buy=prices[0]
        max=0
        for x in prices:
            if x-buy>max:
                max=x-buy
            elif x<buy:
                buy=x
        return max
        