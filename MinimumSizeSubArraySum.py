class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if nums==None or len(nums)==0:
            return 0
        i,j,temp=0,0,0
        res=2**31-1
        for i in xrange(0,len(nums)):
            while j<len(nums) and temp<s:
                temp+=nums[j]
                j+=1
            if temp>=s:
                res=min(res,j-i)
            temp-=nums[i]
        return res if res!=2**31-1 else 0
        
        