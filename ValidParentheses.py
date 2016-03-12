class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)<=1:
            return False
        stack=[]
        for i in range(0,len(s)):
            if s[i]=='('or s[i]=='{' or s[i]=='[':
                stack.append(s[i])
            else:
                if len(stack)==0:
                    return False
                c=stack.pop()
                if c=='(':
                    if s[i]!=')':
                        return False
                if c=='{':
                    if s[i]!='}':
                        return False
                if c=='[':
                    if s[i]!=']':
                        return False
        return len(stack)==0