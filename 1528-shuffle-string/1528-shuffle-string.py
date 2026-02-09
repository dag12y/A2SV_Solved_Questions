class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        l=[' ']*len(s)
        for idx,p in enumerate(indices):
            l[p]=s[idx]
        
        return ''.join(l)