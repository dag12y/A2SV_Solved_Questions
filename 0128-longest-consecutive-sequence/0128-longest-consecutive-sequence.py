class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        _max = max(nums) if nums else 0
        store = [0]*(_max+1)
        
        for num in nums:
            store[num]+=1
        temp=0
        ans=0
        for freq in store:
            if freq:
                temp+=1
            else:
                ans=max(temp,ans)
                temp=0
        return max(ans,temp)
        