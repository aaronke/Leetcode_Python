class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str=str.strip()
        if len(str)==0:
            return 0
        flag,k,result=1,0,0
        if str[0]=='-':
            flag=-1
            k=k+1
        if str[0]=='+':
            flag=1
            k=k+1
        for i in range(k,len(str)):
            if str[i].isdigit():
                result=result*10+int(str[i])
            else:
                break
        if flag*result>2**31-1:
            return 2**31-1
        elif flag*result<-2**31:
            return -2**31
        else:
            return flag*result
            
        
        