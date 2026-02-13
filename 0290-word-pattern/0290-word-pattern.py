class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        from collections import defaultdict
        store=defaultdict(str)
        used=set()
        l=s.split()

        if len(pattern) != len(l):
            return False
        for i in range(len(pattern)):
            if pattern[i] in store:
                if store[pattern[i]] != l[i]:
                    return False
            else:
                if l[i] in used:
                    return False
                store[pattern[i]] = l[i]
                used.add(l[i])
        return True