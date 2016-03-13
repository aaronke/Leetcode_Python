class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result=0
        sign=1 if x>0 else -1
        x=abs(x)
        while x>0:
            result=result*10+x%10
            x=x/10
        return sign*result if sign*result<=2**31-1 and sign* result >=-2**31 else 0
        