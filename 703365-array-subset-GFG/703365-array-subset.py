#User function Template for python3

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        from collections import Counter
    	aDict=dict(Counter(a))
    	bDict=dict(Counter(b))
    	for key,value in bDict.items():
    		if key not in aDict:
    			return False
    		else:
    			if value>aDict[key]:
    				return False
    	return True
        
        
    
    
