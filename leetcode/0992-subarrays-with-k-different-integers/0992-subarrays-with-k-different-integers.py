class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def atMost(k):
            from collections import defaultdict
            count = defaultdict(int)
            left = 0
            res = 0
            
            for right in range(len(nums)):
                count[nums[right]] += 1
                
                while len(count) > k:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        del count[nums[left]]
                    left += 1
                
                res += right - left + 1
            
            return res
        
        return atMost(k) - atMost(k - 1)