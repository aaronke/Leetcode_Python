class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        flag=False
        result=0
        for i in range(len(s)-1,-1,-1):
            c=s[i]
            if c.isalpha():
                flag=True
                result+=1
            else:
                if flag:
                    return result
        return result