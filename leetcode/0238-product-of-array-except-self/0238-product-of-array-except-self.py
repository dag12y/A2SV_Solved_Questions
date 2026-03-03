class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix=1
        res=[1]
        for i in range(1,len(nums)):
            prefix*=nums[i-1]
            res.append(prefix)
        postfix=1
        for i in range(len(nums)-1,-1,-1):
            res[i]=res[i]*postfix
            postfix*=nums[i]
        return res

        