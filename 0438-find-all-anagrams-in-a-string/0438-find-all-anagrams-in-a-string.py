class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
            
        standard = Counter(p)
        window_size = len(p)
        rolling = Counter(s[:window_size]) 
        
        res = []
      
        if rolling == standard:
            res.append(0)
            
      
        for i in range(window_size, len(s)):
            rolling[s[i]] += 1
            left_char = s[i - window_size]
            rolling[left_char] -= 1
            if rolling[left_char] == 0:
                del rolling[left_char]
                
            if rolling == standard:
                res.append(i - window_size + 1)
                
        return res