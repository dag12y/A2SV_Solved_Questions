class Solution(object):
    def twoSum(self, nums, target):
        x=len(nums)
        z=[]
        for i in range(x):
            for j in range(i+1,x):
                if nums[i]+nums[j]==target:
                    z.append(i)
                    z.append(j)
                    return z
        