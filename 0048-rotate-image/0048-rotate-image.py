class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        
        for r in range(row):
            for c in range(col):
                if r < c:
                    matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        for r in range(row):
            matrix[r]=matrix[r][::-1]
        return matrix