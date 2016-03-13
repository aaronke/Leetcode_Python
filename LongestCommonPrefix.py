class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        len_str=len(strs)
        if len_str==0:
            return ''
        if len_str==1:
            return strs[0]
        lengths=[len(i) for i in strs]
        common_prefix=''
        for i in range(min(lengths)):
            temp=strs[0][i]
            for j in range(1,len_str):
                if strs[j][i]!=temp:
                    return common_prefix
            common_prefix+=temp
        return common_prefix
