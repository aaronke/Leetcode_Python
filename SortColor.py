class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        left,right=0,len(nums)-1
        i=0
        while i <=right:
            if nums[i]==0:
                self.swap(nums,left,i)
                left+=1
                i+=1
            elif nums[i]==2:
                self.swap(nums,i,right)
                right-=1
            else:
                i+=1
    def swap(self,nums,left,right):
        temp=nums[left]
        nums[left]=nums[right]
        nums[right]=temp
        
        