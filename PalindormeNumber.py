class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        elif x==0:
            return True
        else:
            y=0
            temp=x
            while x>0:
                y=y*10+x%10
                x=x/10
            if temp==y:
                return True
            else:
                return False
        