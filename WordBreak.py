class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        dp=[False]*(len(s)+1)
        dp[0]=True
        for i in xrange(1,len(s)+1):
            for j in xrange(i-1,-1,-1):
                if dp[j]==True and s[j:i] in wordDict:
                    dp[i]=True
        return dp[len(s)]