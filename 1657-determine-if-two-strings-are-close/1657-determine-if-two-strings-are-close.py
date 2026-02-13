class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        from collections import Counter
        if set(word2) != set(word1):
            return False
        
        freq1 = sorted(Counter(word1).values())
        freq2 = sorted(Counter(word2).values())
        print(freq1)
        print(freq2)
        return freq1 == freq2
