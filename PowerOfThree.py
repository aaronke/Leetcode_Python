from math import log
class Solution(object):
    def isPowerOfThree(self, n):
        return n>0 and n==3**round(math.log(n,3))