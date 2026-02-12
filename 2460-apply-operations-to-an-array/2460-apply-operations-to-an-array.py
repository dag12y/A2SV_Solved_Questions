class Solution(object):
    def applyOperations(self, nums):
        n=len(nums)
        for i in range(n-1):
            if i+1<n and nums[i]==nums[i+1]:
                nums[i] *= 2  
                nums[i + 1] = 0 
        for i in range(n-1,-1,-1):
            if nums[i]==0:
                x=nums.pop(i)
                nums.append(x)
        return nums
        