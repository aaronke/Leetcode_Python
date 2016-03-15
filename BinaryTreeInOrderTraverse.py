# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result=[]
        if root==None:
            return result
        stack=[]
        node=root
        while node!=None or len(stack)!=0:
            while node!=None:
                stack.append(node)
                node=node.left
            if len(stack)!=0:
                node=stack.pop()
                result.append(node.val)
                node=node.right
        return result
        