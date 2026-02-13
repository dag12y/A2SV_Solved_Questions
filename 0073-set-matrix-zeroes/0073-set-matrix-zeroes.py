class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows=set()
        cols=set()
        
        row = len(matrix)
        col = len(matrix[0])
        
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 0:
                    rows.add(r)
                    cols.add(c)
        for r in rows:
            matrix[r]=[0]*col
        for c in cols:
            for r in range(row):
                matrix[r][c]=0
        print(matrix)