class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        rows = len(mat)
        cols = len(mat[0])
        startRow = 0
        startCol = 0
        up = True
        ans=[]
        while len(ans)<rows*cols:
            ans.append(mat[startRow][startCol])
            if not up:
                if startRow == rows -1:
                    startCol+=1
                    up=True
                elif startCol == 0:
                    startRow+=1
                    up=True
                else:
                    startRow+=1
                    startCol-=1
            else:
                if startCol == cols -1:
                    startRow+=1
                    up=False
                elif startRow == 0:
                    startCol+=1
                    up=False
                else:
                    startRow-=1
                    startCol+=1
        return ans