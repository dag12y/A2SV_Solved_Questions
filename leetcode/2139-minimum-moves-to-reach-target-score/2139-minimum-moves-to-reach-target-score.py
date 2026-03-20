class Solution(object):
    def minMoves(self, target, maxDoubles):
        """
        :type target: int
        :type maxDoubles: int
        :rtype: int
        """
        ans = 0
        while target>1:
            if maxDoubles == 0:
                ans+=target-1
                break
            if target %2 == 0:
                maxDoubles-=1
                target = target // 2
                ans+=1
                continue
            else:
                ans+=1
                target-=1
        return ans

        