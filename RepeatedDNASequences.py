class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res=set()
        if s==None or len(s)<=10:
            return list(res)
        m=set()
        for i in xrange(len(s)-9):
            substring=s[i:i+10]
            if substring in m:
                res.add(substring)
            else:
                m.add(substring)
        return list(res)