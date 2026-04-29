class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows,cols = len(board),len(board[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        def dfs(r,c):
            if (r<0 or r>=rows or c<0 or c>=cols or board[r][c] != "O"):
                return
            board[r][c] = 'C'
            for dr,dc in directions:
                dfs(r+dr,c+dc)
        
        # (dfs) capture unsurrounded regions O -> C   
        for r in range(rows):
            for c in range(cols):
                if (r in [0,rows-1] or c in [0,cols-1]) and board[r][c] == "O":
                    dfs(r,c)
             
        # capture surrounded regions O -> X
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        # uncapture unsurrounded regions C -> O
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "C":
                    board[r][c] = "O"
        
