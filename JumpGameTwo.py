class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curmax,premax,jump=0,0,0
        i=0
        while curmax<len(nums)-1:
            premax=curmax
            while i<=premax:
                curmax=max(curmax,i+nums[i])
                i+=1
            jump+=1
            if premax==curmax: return -1
        return jump
                
        