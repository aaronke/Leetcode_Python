class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]
        self.minStack=[]
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        if self.getMin()>=x:
            self.minStack.append(x)
        self.stack.append(x)
        

    def pop(self):
        """
        :rtype: nothing
        """
        if self.stack.pop()==self.getMin():
            self.minStack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[len(self.stack)-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.minStack)==0:
            return 2**31
        else:
            return self.minStack[len(self.minStack)-1]
        