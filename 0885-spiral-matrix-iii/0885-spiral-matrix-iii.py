class Solution(object):
    def spiralMatrixIII(self, rows, cols, rStart, cStart):
        """
        :type rows: int
        :type cols: int
        :type rStart: int
        :type cStart: int
        :rtype: List[List[int]]
        """
        total = rows * cols
        ans = []

        # directions: right, down, left, up
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        r, c = rStart, cStart
        if 0 <= r < rows and 0 <= c < cols:
            ans.append([r, c])

        step = 1  # step size for current leg pair
        d = 0     # direction index

        while len(ans) < total:
            for _ in range(2):  # same step length for two directions
                dr, dc = dirs[d % 4]
                for _ in range(step):
                    r += dr
                    c += dc
                    if 0 <= r < rows and 0 <= c < cols:
                        ans.append([r, c])
                        if len(ans) == total:
                            return ans
                d += 1
            step += 1

        return ans