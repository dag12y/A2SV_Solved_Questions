class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        _max = 0
        sortedNums = sorted(nums)
        for i in range(len(sortedNums)-2):
            if sortedNums[i]+sortedNums[i+1] > sortedNums[i+2]:
                _max = max(_max,sum(sortedNums[i:i+3]))
        return _max
        