class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result=[0]*(len(nums)+1)

        for num in nums:
            result[num]+=1
        
        for i,val in enumerate(result):
            if val!=2:
                result[i]=0
        j=0
        for i in range(len(result)):
            if result[i]!=0:
                result[j]=i
                result[i]=0
                j+=1
        return result[:j]
        
        
        