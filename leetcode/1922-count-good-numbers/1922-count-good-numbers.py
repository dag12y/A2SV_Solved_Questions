class Solution(object):
    def countGoodNumbers(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7
        
        def power(base, exp):
            if exp == 0:
                return 1
            
            half = power(base, exp // 2)
            
            if exp % 2 == 0:
                return (half * half) % MOD
            else:
                return (half * half * base) % MOD
        
        even = (n + 1) // 2
        odd = n // 2
        
        return (power(5, even) * power(4, odd)) % MOD


        