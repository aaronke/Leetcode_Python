class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if nums==None or len(nums)==0:
            return False
        left,right=0,len(nums)-1
        while left<=right:
            mid=left+(right-left)/2
            if nums[mid]==target or nums[left]==target or nums[right]==target:
                return True
            if nums[mid]<nums[right]:
                if target>nums[mid] and target<nums[right]:
                    left=mid+1
                else:
                    right=mid-1
            elif nums[mid]==nums[right]:
                right-=1
            else:
                if target>nums[left] and target<nums[mid]:
                    right=mid-1
                else:
                    left=mid+1
        return False