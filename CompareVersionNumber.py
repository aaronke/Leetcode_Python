class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        varr1=version1.split(".")
        varr2=version2.split(".")
        len1=len(varr1)
        len2=len(varr2)
        lenMax=max(len1,len2)
        for x in range(lenMax):
            v1=0
            if x<len1:
                v1=int(varr1[x])
            v2=0
            if x<len2:
                v2=int(varr2[x])
            if v1<v2:
                return -1
            if v1>v2:
                return 1
        return 0
        