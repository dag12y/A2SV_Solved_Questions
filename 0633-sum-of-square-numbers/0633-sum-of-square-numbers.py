class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        a,b = 1,1
        n=int(c**0.5)+1
        while a<n and b<n:
            if a**2 + b**2 == c:
                return True
            elif a**2 + b**2 < c:
                a+=1
            else:
                b-=1
            
        return False
        