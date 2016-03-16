class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans=[0]*(n+1)
        ans[0]=1
        for i in range(1,n+1):
            for j in range(0,i):
                ans[i]+=ans[j]*ans[i-j-1]
        return ans[n]
        