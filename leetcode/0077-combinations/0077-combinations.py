class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        
        def backtrack(start, path):
            # base case
            if len(path) == k:
                res.append(path[:])
                return
            
            # try choices
            for i in range(start, n + 1):
                if len(path) + (n - i + 1) < k:
                    break
                path.append(i)           # choose
                backtrack(i + 1, path)  # go deeper
                path.pop()              # undo (backtrack)
        
        backtrack(1, [])
        return res