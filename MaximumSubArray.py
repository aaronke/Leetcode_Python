class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums==None or len(nums)==0:
            return 0
        curSum=-2**31
        ans=nums[0]
        for x in nums:
            curSum=max(curSum+x,x)
            ans=max(curSum,ans)
        return ans
        
        