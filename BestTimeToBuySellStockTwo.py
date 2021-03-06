class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)==0:
            return 0
        max=0
        for i in xrange(1,len(prices)):
            if prices[i]>prices[i-1]:
                max+=prices[i]-prices[i-1]
        return max
        