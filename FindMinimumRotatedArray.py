class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums==None or len(nums)==0:
            return -1
        if len(nums)==1:
            return nums[0]
        left,right=0,len(nums)-1
        while left<right:
            mid=left+(right-left)/2
            if nums[mid]<=nums[right]:
                right=mid
            else:
                left=mid+1
        return nums[left]
        