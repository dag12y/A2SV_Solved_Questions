# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        def dfs(node,_max):
            nonlocal ans
            if not node:
                return None
            if node.val >= _max:
                ans+=1
                _max = node.val
            dfs(node.left,_max)
            dfs(node.right,_max)
        dfs(root,float("-inf"))
        return ans