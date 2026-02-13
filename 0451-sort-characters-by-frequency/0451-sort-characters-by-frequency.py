class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import Counter
        store = Counter(s)
        print(store)
        ans = ''.join(ch * freq for ch, freq in store.most_common())
        return ans