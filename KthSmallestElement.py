# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        index=0
        stack=[]
        node=root
        while node!=None or len(stack)!=0:
            while(node!=None):
                stack.append(node)
                node=node.left
            if len(stack)!=0:
                node=stack.pop()
                index+=1
                if index==k:
                    return node.val
                node=node.right
        return 0
        
        