class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        from collections import defaultdict
        store = defaultdict(int)
        
        for num in nums:
            store[num]+=1
            if store[num]==2:
                return True
        return False

        