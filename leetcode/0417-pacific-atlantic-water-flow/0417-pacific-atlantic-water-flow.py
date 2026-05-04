class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        rows,cols = len(heights),len(heights[0])
        #visted
        pacific = set()
        atlantic = set()

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        # from edges
        def dfs(r,c,visited):
            visited.add((r,c))

            for dr,dc in directions:
                R = r+dr
                C = c+dc
                if 0<=R<rows and 0<=C<cols and (R,C) not in visited and heights[R][C] >= heights[r][c]:
                    dfs(R,C,visited)
        # run from edges
        for c in range(cols):
            dfs(0,c,pacific)
            dfs(rows-1,c,atlantic)
        for r in range(rows):
            dfs(r,0,pacific)
            dfs(r,cols-1,atlantic)
        ans = pacific.intersection(atlantic)
        return list(ans)
        


        