class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        from collections import defaultdict
        ans = defaultdict(int)
        temp = sorted(nums)
        
        for i in range(len(temp)):
            if temp[i]!=temp[i-1]:
                ans[temp[i]] = i

        res=[]
        for num in nums:
            res.append(ans[num])
        return res
        
            