# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack=[]
        self.pushLeft(root)
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack)!=0
        

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            p=self.stack.pop()
        else:
            return []
        self.pushLeft(p.right)
        return p.val
    def pushLeft(self,node):
        while node:
            self.stack.append(node)
            node=node.left
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())