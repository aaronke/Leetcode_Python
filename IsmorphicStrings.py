class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ms=[0]*256
        mt=[0]*256
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            if ms[ord(s[i])]!=mt[ord(t[i])]:
                return False
            else:
                ms[ord(s[i])]=i+1
                mt[ord(t[i])]=i+1
        return True
            
        