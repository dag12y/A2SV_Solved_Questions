class Solution:
    def minOperations(self, nums):
        
        count = 0
        for i in range(len(nums)-2):
            if nums[i] == 0:
                count+=1
                nums[i] = 1
                nums[i+1] = (0 if nums[i+1] else 1)
                nums[i+2] = (0 if nums[i+2] else 1)
        print(nums[i:])
        if sum(nums[i:]) == 3:
            return count
        else:
            return -1