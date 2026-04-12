class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        operations = 0
        
        # Start from right
        prev = nums[-1]
        
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] <= prev:
                prev = nums[i]
            else:
                # number of parts
                k = (nums[i] + prev - 1) // prev  # ceil division
                
                operations += k - 1
                
                # update prev to the maximum allowed value after split
                prev = nums[i] // k
        
        return operations