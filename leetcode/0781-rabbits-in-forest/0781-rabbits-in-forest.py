class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        ans = 0
        for key,val in count.items():
            size = key+1
            groups = (val+key)//size
            ans+=groups*size
        return ans