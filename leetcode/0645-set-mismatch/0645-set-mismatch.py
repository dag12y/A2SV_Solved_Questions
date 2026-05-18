class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen = set()
        duplicate = -1
        
        for num in nums:
            if num in seen:
                duplicate = num
            seen.add(num)
        
        n = len(nums)
        diff = sum(nums) - (n*(n+1)//2)
        missing = duplicate - diff
        
        return [duplicate, missing]
