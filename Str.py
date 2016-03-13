class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack==None or needle==None or len(needle)==0:
            return 0
        for i in range(0,len(haystack)-len(needle)+1):
            temp=i
            for j in range(0,len(needle)):
                if needle[j]!=haystack[temp]:
                    break
                temp+=1
                if j==len(needle)-1:
                    return i
        return -1
                    
        