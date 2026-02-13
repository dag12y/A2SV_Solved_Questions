class Solution(object):
    def findCommonResponse(self, responses):
        """
        :type responses: List[List[str]]
        :rtype: str
        """
        from collections import Counter
	
        newResponses = []
        for i in range(len(responses)):
            newResponse = list(set(responses[i]))
            newResponses.extend(newResponse)	
    
        store = Counter(newResponses)
        maxFreq = max(store.values())
    
        ans = [key for key,val in store.items() if val==maxFreq]
        ans.sort()
        return ans[0] 
            