class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        values = {
		'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000
        }
        romans={'IV':2,'IX':2,'XL':20,'XC':20,'CD':200,'CM':200}
        
        num=0
        for l in s:
            num+=values[l]
        for roman in romans:
            if roman in s:
                num-=romans[roman]
        return num
            