# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res=[]
        if root==None: return res
        temp=[root.val]
        self.dfs(root,res,temp,sum-root.val)
        return res
    def dfs(self,root,res,temp,sum):
        if root==None: return
        if root.left==None and root.right==None and sum==0:
            res.append(temp)
        if root.left!=None:
            self.dfs(root.left,res,temp+[root.left.val],sum-root.left.val)
        if root.right!=None:
            self.dfs(root.right,res,temp+[root.right.val],sum-root.right.val)
        
        