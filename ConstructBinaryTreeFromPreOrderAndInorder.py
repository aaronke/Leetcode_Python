# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return self.construct(preorder,0,len(preorder)-1,inorder,0,len(inorder)-1)
    
    def construct(self,preorder,preStart,preEnd,inorder,inStart,inEnd):
        if preEnd<preStart or inEnd<inStart:
            return None
        val=preorder[preStart]
        k=0
        for i in xrange(0,len(inorder)):
            if inorder[i]==val:
                k=i
                break
        p=TreeNode(val)
        p.left=self.construct(preorder,preStart+1,preStart+k-inStart,inorder,inStart,k-1)
        p.right=self.construct(preorder,preStart+k-inStart+1,preEnd,inorder,k+1,inEnd)
        return p
        
        