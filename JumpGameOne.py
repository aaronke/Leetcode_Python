class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums==None or len(nums)<=1:
            return True
        max=nums[0]
        for i in xrange(0,len(nums)):
            if max==i and nums[i]==0:
                return False
            if max<nums[i]+i:
                max=nums[i]+i;
            if max>=len(nums)-1:
                return True
                
        