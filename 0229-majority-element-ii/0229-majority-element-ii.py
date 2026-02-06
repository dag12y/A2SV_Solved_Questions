class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        d = dict(Counter(nums))
        ans=[]
        n=len(nums)
        for key,val in d.items():
            if val>n/3:
                ans.append(key)
        return ans
        