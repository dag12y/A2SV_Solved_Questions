class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        posDiag = set() # r+c is constant
        negDiag = set() # r-c is constant

        res = 0
        def backtrack(r):
            if r == n:
                nonlocal res
                res+=1
                return
            for c in range(n):
                if c in col or (r+c) in posDiag or (r-c)  in negDiag:
                    continue

                col.add(c)
                negDiag.add(r-c)
                posDiag.add(r+c)

                backtrack(r+1)

                col.remove(c)
                negDiag.remove(r-c)
                posDiag.remove(r+c)
        backtrack(0)

        return res


