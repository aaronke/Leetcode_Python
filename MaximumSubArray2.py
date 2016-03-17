class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums==None or len(nums)==0:
            return None
        return self.helper(nums,0,len(nums)-1)
        
    def helper(self,nums,left,right):
        if left>=right:
            return nums[left]
        mid=left+(right-left)/2
        lmax=self.helper(nums,left,mid-1)
        rmax=self.helper(nums,mid+1,right)
        cmax=max(lmax,rmax)
        lsum,clmax=0,0
        for i in range(mid-1,left-1,-1):
            lsum+=nums[i]
            if lsum>clmax:
                clmax=lsum
        rsum,crmax=0,0
        for i in range(mid+1,right+1):
            rsum+=nums[i]
            if rsum>crmax:
                crmax=rsum
        return max(cmax,clmax+nums[mid]+crmax)
                
        
        
        