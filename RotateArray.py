class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        if len(nums)==0:
            return
        mid=len(nums)-k
        self.reverse(nums,0,mid-1)
        self.reverse(nums,mid,len(nums)-1)
        self.reverse(nums,0,len(nums)-1)
        
    def reverse(self,nums,left,right):
        if nums==None or len(nums)==0:
            return
        while left<right:
            temp=nums[right]
            nums[right]=nums[left]
            nums[left]=temp
            left+=1
            right-=1
        
        