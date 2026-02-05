class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        ans=0
        for word in words:
            if set(word).issubset(set(chars)):
                ans+=len(word)
        return ans


        