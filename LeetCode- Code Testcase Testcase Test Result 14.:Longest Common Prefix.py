class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result=''
        for i in range(len(strs[0])):
            curr = strs[0][i]  # curr=s
            same=True
            for j in range(1,len(strs)): 
                if i>=len(strs[j]):
                    return result
                same = same and (strs[j][i]==curr)
            if same : result+=curr
            else:break
        return result
            

