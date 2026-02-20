class Solution(object):
    def minimumIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        freq = Counter(nums)

        # Step 1: find global dominant element
        dominant = -1
        total_count = 0
        for num, count in freq.items():
            if count * 2 > n:
                dominant = num
                total_count = count
                break

        if dominant == -1:
            return -1

        # Step 2: scan for valid split
        left_count = 0
        for i in range(n - 1):
            if nums[i] == dominant:
                left_count += 1

            left_len = i + 1
            right_len = n - left_len

            if (left_count * 2 > left_len and
                (total_count - left_count) * 2 > right_len):
                return i

        return -1