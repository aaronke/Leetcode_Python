class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums==None or len(nums)==0:
            return 0
        dp=[1]*len(nums)
        for i in xrange(1,len(nums)):
            for j in xrange(0,i):
                if nums[j]<nums[i]:
                    dp[i]=max(dp[j]+1,dp[i])
        return max(dp)
        