class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        def backtrack(start, path):
            res.append(path[:])  # save current subset
            
            for i in range(start, len(nums)):
                path.append(nums[i])        # choose
                backtrack(i + 1, path)     # move forward
                path.pop()                 # undo
        
        backtrack(0, [])
        return res