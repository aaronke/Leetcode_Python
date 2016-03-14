class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s=0
        for x in nums:
            s^=x
        y=s&(-s)
        result=[0,0]
        for x in nums:
            if (x & y)!=0:
                result[0] ^= x
            else:
                result[1] ^= x
        return result
            
        