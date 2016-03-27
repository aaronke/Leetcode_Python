class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        index1,index2=0,0
        for i in xrange(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                index1=i
                break
        for i in xrange(len(nums)-1,index1,-1):
            if nums[i]>nums[index1]:
                index2=i
                break
        if index1==0 and index2==0:
            self.reverse(0,len(nums)-1,nums)
            return
        temp=nums[index1]
        nums[index1]=nums[index2]
        nums[index2]=temp
        self.reverse(index1+1,len(nums)-1,nums)
    
    def reverse(self,start,end,nums):
        while start<end:
            temp=nums[start]
            nums[start]=nums[end]
            nums[end]=temp
            start+=1
            end-=1
        