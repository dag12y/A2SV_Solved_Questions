class Solution(object):
    def findRotation(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: List[List[int]]
        :rtype: bool
        """
        n=len(mat)
        def rotateMatrix(matrix):
            ans=[[0 for _ in range(n)] for _ in range(n)]
            for r in range(n):
                for c in range(n):
                    ans[r][c]=matrix[c][r]
            for r in range(n):
                ans[r] = ans[r][::-1]
            return ans
        newMat=rotateMatrix(mat)
        
        if newMat == target:
            return True
        
        for _ in range(3):
            newMat = rotateMatrix(newMat)
            if newMat == target:
                return True
        return False
            