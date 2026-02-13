class Solution(object):
    def minimumSwap(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        xy,yx=0,0
        for a,b in zip(s1,s2):
            if a=='x' and b == 'y':
                xy+=1
            elif a=='y' and b == 'x':
                yx+=1
        # mismatch can not be odd
        if (xy+yx)%2 != 0:
            return -1
        
        #pairs of same type and remaining unmatched
        swaps = xy//2 +yx//2 + xy%2 *2
        
        return swaps