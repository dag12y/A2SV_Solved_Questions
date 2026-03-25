class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        
        def backtrack(path, remaining):
            if not remaining:
                res.append(path[:])
                return
            
            for i in range(len(remaining)):
                # choose
                path.append(remaining[i])
                
                # explore
                backtrack(path, remaining[:i] + remaining[i+1:])
                
                # unchoose (backtrack)
                path.pop()
        
        backtrack([], nums)
        return res