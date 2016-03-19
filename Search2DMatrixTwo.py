class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix==None or len(matrix)==0:
            return False
            
        return self.helper(matrix,0,len(matrix)-1,0,len(matrix[0])-1,target)
        
    def helper(self,matrix,rowS,rowE,colS,colE,target):
        if rowS>rowE or colS>colE:
            return False
        rowM=rowS+(rowE-rowS)/2
        colM=colS+(colE-colS)/2
        if matrix[rowM][colM]==target:
            return True
        elif matrix[rowM][colM]<target:
            return self.helper(matrix,rowS,rowM,colM+1,colE,target)\
            or self.helper(matrix,rowM+1,rowE,colS,colM,target)\
            or self.helper(matrix,rowM+1,rowE,colM+1,colE,target)
        else:
            return self.helper(matrix,rowS,rowM-1,colS,colM-1,target) \
            or self.helper(matrix,rowM,rowE,colS,colM-1,target) \
            or self.helper(matrix,rowS,rowM-1,colM,colE,target)