class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        # Convert integers to strings
        nums = list(map(str, nums))

        # Custom comparator
        def compare(a, b):
            if a + b > b + a:
                return -1   # a should come before b
            elif a + b < b + a:
                return 1    # b should come before a
            else:
                return 0

        # Sort using custom comparator
        nums.sort(key=cmp_to_key(compare))

        # Edge case: when all numbers are "0"
        if nums[0] == "0":
            return "0"

        return "".join(nums)
        