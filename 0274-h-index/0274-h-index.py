class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        h=0
        citations.sort(reverse=True)
        for i,n in enumerate(citations):
            if n>=i+1:
                h+=1
            else:
                break
                
        return h