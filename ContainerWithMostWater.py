class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left,right=0,len(height)-1
        res=0
        pre=0
        while left<right:
            res=max(res,(right-left)*min(height[left],height[right]))
            if height[left]<height[right]:
                pre=left
                while left<right and height[left]<=height[pre]:
                    left+=1
            else:
                pre=right
                while left<right and height[right]<=height[pre]:
                    right-=1
        return res
        