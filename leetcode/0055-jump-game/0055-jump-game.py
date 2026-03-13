class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        far = 0
        for curr in range(len(nums)):
            if curr > far:
                return False
            far = max(far,curr+nums[curr])
        return True
        