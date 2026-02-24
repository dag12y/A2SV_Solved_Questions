class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        from collections import Counter
        store = Counter(s)
        ans=[]
        for l in order:
            if store.get(l,False):
                ans.append(l*store[l])
                del store[l]
                
        excluded = list(key*val for key,val in store.items())
        ans.extend(excluded)
        res = ''.join(ans)
        
        return res
        