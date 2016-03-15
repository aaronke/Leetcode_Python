class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=0
        for i in range(0,len(nums)):
            ans+=i+1-nums[i]
        return ans
        
    def missingNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=0
        for x in xrange(0,len(nums)+1):
            ans^=x
        for i in range(0,len(nums)):
            ans^=nums[i]
        return ans