class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        ans = []
        for key,val in count.items():
            if val == 2:
                ans.append(key)
        return ans