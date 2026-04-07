class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def can(x):
            count = 0
            for c in candies:
                count+=c // x
            return count >= k
        left = 1
        right = max(candies)
        ans =0
        while left <= right:
            mid = left + (right-left)//2
            if can(mid):
                ans = mid
                left = mid+1
            else:
                right = mid -1
        return ans