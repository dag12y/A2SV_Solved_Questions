class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
        _min = min(nums)
        return 1 if _min > 0 else 1-_min