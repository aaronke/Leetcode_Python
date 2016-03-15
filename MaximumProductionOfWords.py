class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        if len(words)==0:
            return 0
        m=len(words)
        ans=0
        temps=[0]*m
        for i in xrange(0,m):
            for j in xrange(0,len(words[i])):
                temps[i]|=1<<(ord(words[i][j])-97)
        for i in xrange(0,m):
            for j in xrange(i+1,m):
                if temps[i]&temps[j]==0:
                    ans=max(ans,len(words[i])*len(words[j]))
        return ans
                    
        