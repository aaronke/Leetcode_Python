class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res=[]
        self.helper(res,n,n,"")
        return res
    
    def helper(self,res,left,right,item):
        if left==0 and right==0:
            res.append(item)
        if left>0:
            self.helper(res,left-1,right,item+"(")
        if right>0 and left<right:
            self.helper(res,left,right-1,item+")")
        
    
        