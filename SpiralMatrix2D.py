class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        result=[[0 for i in range(n)] for j in range(n)]
        row,col=n,n
        index=1
        x,y=0,0
        while index<=n*n and col>0 and row>0:
            if row==1 and col==1:
                result[x][y]=index
                index+=1
            for i in xrange(0,col-1):
                result[x][y]=index
                y+=1
                index+=1
            for i in xrange(0,row-1):
                result[x][y]=index
                x+=1
                index+=1
            for i in xrange(0,col-1):
                result[x][y]=index
                index+=1
                y-=1
            for i in xrange(0,row-1):
                result[x][y]=index
                index+=1
                x-=1
            col-=2
            row-=2
            x+=1
            y+=1
        return result
                
                
        
        