class Solution(object):
    def findValidPair(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import Counter
        store = dict(Counter(s))
        for i in range(len(s)-1):
            a,b = s[i],s[i+1]
            if(a!=b and store[a] == int(a) and store[b] == int(b)):
                return a+b
       
        return ''
        