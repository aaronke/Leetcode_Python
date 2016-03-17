# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        return self.construct(inorder,0,len(inorder)-1,postorder,0,len(postorder)-1)
        
    def construct(self,inorder,inStart,inEnd,postorder,postStart,postEnd):
        if inStart>inEnd or postStart>postEnd:
            return None
        val= postorder[postEnd]
        k=0
        for i in xrange(0,len(inorder)):
            if inorder[i]==val:
                k=i
                break
        p=TreeNode(val)
        p.left=self.construct(inorder,inStart,k-1,postorder,postStart,postStart+k-1-inStart)
        p.right=self.construct(inorder,k+1,inEnd,postorder,postStart+k-inStart,postEnd-1)
        return p
        