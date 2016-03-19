class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if matrix==None or len(matrix)==0:
            return
        m=len(matrix)
        n=len(matrix[0])
        fcol,frow=False,False
        for i in xrange(0,m):
            if matrix[i][0]==0:
                fcol=True
                break
        for i in xrange(0,n):
            if matrix[0][i]==0:
                frow=True
                break
        for i in xrange(1,m):
            for j in xrange(1,n):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0
        for i in xrange(1,m):
            if matrix[i][0]==0:
                for j in xrange(0,n):
                    matrix[i][j]=0
        for j in xrange(1,n):
            if matrix[0][j]==0:
                for i in xrange(0,m):
                    matrix[i][j]=0
        if fcol:
            for i in xrange(0,m):
                matrix[i][0]=0
        if frow:
            for i in xrange(0,n):
                matrix[0][i]=0
            
                
        