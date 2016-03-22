class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums==None or len(nums)==0:
            return [-1,-1]
        start,end=0,len(nums)-1
        while start<=end:
            mid=start+(end-start)/2
            if nums[mid]==target:
                left,right=mid-1,mid+1
                while left>=0 and nums[left]==target:
                    left-=1
                while right<len(nums) and nums[right]==target:
                    right+=1
                return [left+1,right-1]
            if nums[mid]<target:
                start=mid+1
            else:
                end=mid-1
        return [-1,-1]
        