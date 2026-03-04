from collections import defaultdict
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = defaultdict(int)
        left = 0
        ans=0
        for right in range(len(s)):
            count[s[right]]+=1
            while (right-left+1) - max(count.values()) > k:
                count[s[left]]-=1
                left+=1
            ans = max(ans, right-left+1)
        return ans