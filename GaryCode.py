class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res=[]
        res.append(0)
        for i in xrange(0,n):
            highestBit=1<<i
            preLen=len(res)
            for j in xrange(preLen-1,-1,-1):
                res.append(highestBit+res[j])
        return res
        
        
        