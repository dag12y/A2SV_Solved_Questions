class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        sortedPiles = sorted(piles)
        n = len(piles) // 3
        ans=0
        for i in range(n):
            ans+=sortedPiles[n+(i*2)]
        return ans

