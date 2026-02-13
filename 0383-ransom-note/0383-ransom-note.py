class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        count = [0]*26

        for letter in ransomNote:
            count[ord(letter)-97]+=1
        for letter in magazine:
            count[ord(letter)-97]-=1
        for val in count:
            if val > 0:
                return False
        return True
        