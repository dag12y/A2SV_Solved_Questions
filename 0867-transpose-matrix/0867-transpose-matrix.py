class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        row = len(matrix)
        col = len(matrix[0])
        
        newMatrix = [[0 for _ in range(row)] for _ in range(col)] 
        
        for r in range(row):
            for c in range(col):
                newMatrix[c][r] = matrix[r][c]
    
        return newMatrix
        