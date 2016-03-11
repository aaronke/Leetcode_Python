class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result=[]
        init=1
        for i in range(0,rowIndex):
            result.append(init)
            init=init*(rowIndex-i)/(i+1)
        result.append(1)
        return result
        