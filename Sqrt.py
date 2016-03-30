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
    def mySqrt2(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<=1:
            return x
        left=1
        right=x
        while left<right:
            mid=left+(right-left)/2
            if mid*mid<=x:
                left=mid+1
            else:
                right=mid;
        return left-1