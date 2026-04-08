class Solution:
    def splitString(self, s: str) -> bool:
        def dfs(index, prev, count):
            # if we used all digits and have at least 2 numbers
            if index == len(s):
                return count >= 2
            
            num = 0
            for i in range(index, len(s)):
                num = num * 10 + int(s[i])
                
                # first number → always allowed
                if prev == -1:
                    if dfs(i + 1, num, count + 1):
                        return True
                else:
                    # must be exactly prev - 1
                    if num == prev - 1:
                        if dfs(i + 1, num, count + 1):
                            return True
                    
                    # optimization: stop if too big
                    if num >= prev:
                        break
            
            return False

        return dfs(0, -1, 0) 