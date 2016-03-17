class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        N=m+n-1-1
        k=min(m,n)-1
        res=1
        for i in xrange(0,k):
            res=res*(N-i)/(i+1)
        return res