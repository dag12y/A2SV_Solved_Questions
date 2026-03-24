"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        ans=[]
        path = [root.val]

        def preorder(node):
            if not node:
                return 
            ans.append(node.val)
            for child in node.children:
                path.append(child.val)
                preorder(child)
                path.pop()
            # if not node.children :
            #     print(path)

        preorder(root)

        return ans



            



        