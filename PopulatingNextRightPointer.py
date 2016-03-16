# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        p=root
        first=None
        while p!=None:
            if first==None:
                first=p.left
            if p.left!=None:
                p.left.next=p.right
            else:
                break
            if p.next!=None:
                p.right.next=p.next.left
                p=p.next
            else:
                p=first
                first=None
            
        