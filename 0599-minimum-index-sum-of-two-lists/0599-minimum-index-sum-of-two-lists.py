class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        temp={}
        for i,word in enumerate(list1):
            if word in list2:
                temp[word]=i+list2.index(word)
        
        minVal=min(temp.values())
        
        ans=[ word for word in temp if temp[word]==minVal]
        return ans