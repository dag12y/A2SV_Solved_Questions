class Solution(object):
    def maxSumRangeQuery(self, nums, requests):
        """
        :type nums: List[int]
        :type requests: List[List[int]]
        :rtype: int
        """
        n = len(nums)
        
        # Step 1: Build frequency array
        freq = [0] * (n + 1)
        
        for l, r in requests:
            freq[l] += 1
            if r + 1 < n:
                freq[r + 1] -= 1
        
        # Prefix sum to get actual frequencies
        for i in range(1, n):
            freq[i] += freq[i - 1]
        
        freq = freq[:n]
        
        # Step 2: Sort both arrays
        nums.sort()
        freq.sort()
        
        # Step 3: Compute result
        result = 0
        for i in range(n):
            result = (result + nums[i] * freq[i]) % (10**9 + 7)
        
        return result