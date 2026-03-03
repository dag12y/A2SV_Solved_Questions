class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        row = len(matrix)
        col = len(matrix[0])
        for i in range(row):
            for j in range(col):
                if i>0:
                    matrix[i][j]+=matrix[i-1][j]
                if j>0:
                    matrix[i][j]+=matrix[i][j-1]
                if i>0 and j>0:
                    matrix[i][j]-=matrix[i-1][j-1]
        self.matrix = matrix
                
        

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        
        ans = self.matrix[row2][col2]
        if row1>0:
            ans-=self.matrix[row1-1][col2]
        if col1>0:
            ans-=self.matrix[row2][col1-1]
        if row1>0 and col1>0:
            ans+=self.matrix[row1-1][col1-1]
        return ans
    

        


# Your NumMatrix object will be instantiated and called as such:
matrix = [[-4, -5]]
row1 = 0
col1 = 0
row2 = 0
col2 = 1
obj = NumMatrix(matrix)
param_1 = obj.sumRegion(row1,col1,row2,col2)
print(param_1)