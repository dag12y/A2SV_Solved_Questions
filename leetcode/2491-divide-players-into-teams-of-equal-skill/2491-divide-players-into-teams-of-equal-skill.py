class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        skill.sort()
        start,end=0,len(skill)-1
        target_sum=skill[start]+skill[end]
        ans=0
        while start<end:
            add=skill[start]+skill[end]
            if(target_sum!=add):
                return -1
            else:
                ans+=skill[start]*skill[end]
                start+=1
                end-=1
        return ans
        