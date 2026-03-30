class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def backtrack(l, r):
            if l == r:
                return nums[l]
            
            pick_left = nums[l] - backtrack(l+1, r)
            pick_right = nums[r] - backtrack(l, r-1)
            
            return max(pick_left, pick_right)
        
        return backtrack(0, len(nums)-1) >= 0