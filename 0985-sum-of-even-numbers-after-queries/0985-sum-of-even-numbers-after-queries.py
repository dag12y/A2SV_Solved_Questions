class Solution(object):
    def sumEvenAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        ans=[]
        
        for val,idx in queries:
            nums[idx]=nums[idx]+val
            temp=map(lambda x:0 if x%2 else x,nums)
            ans.append(sum(temp))
        return ans
                
            