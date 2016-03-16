# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.getTree(nums,0,len(nums)-1)
    
    def getTree(self,nums,start,end):
        if start>end:
            return None
        mid=start+(end-start)/2
        head=TreeNode(nums[mid])
        head.left=self.getTree(nums,start,mid-1)
        head.right=self.getTree(nums,mid+1,end)
        return head
        