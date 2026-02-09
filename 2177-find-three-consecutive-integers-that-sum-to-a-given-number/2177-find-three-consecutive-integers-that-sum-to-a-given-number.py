class Solution(object):
    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        x=(num-3)//3 
        isInteger=(num-3)%3 == 0
        if(isInteger):
            return [x,x+1,x+2]
        return []