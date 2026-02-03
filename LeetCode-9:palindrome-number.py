class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        stringX=str(x)
        reverseX=stringX[::-1]

        return stringX==reverseX
        

        
