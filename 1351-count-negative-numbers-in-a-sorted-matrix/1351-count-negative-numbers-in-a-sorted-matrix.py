class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        store=[]
        row = len(grid)
        ans=0
        
        for r in range(row):
            store.extend(grid[r])
        
        for num in store:
            if num<0:
                ans+=1
        return ans