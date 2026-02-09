class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s=[str(num) for num in nums]
        temp = ''.join(s)
        return [int(l) for l in temp]

        