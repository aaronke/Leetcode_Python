class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==0:
            return 0
        start=1.0
        while abs(start*start-x)>0.01:
            start=(start+x/start)/2
        return int(start)
        