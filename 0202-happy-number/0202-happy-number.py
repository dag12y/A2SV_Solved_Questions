class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen=[]

        while len(seen) == len(set(seen)):
            if 1 in seen:
                return True
            
            t=[int(digit) for digit in str(n)]
            n = sum(map(lambda x:x**2,t))
            seen.append(n)
        return False
            