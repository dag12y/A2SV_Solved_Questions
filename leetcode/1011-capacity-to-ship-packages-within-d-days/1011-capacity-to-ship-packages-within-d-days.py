class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(capacity):
            days_used = 1
            current = 0
            
            for w in weights:
                if current + w > capacity:
                    days_used += 1
                    current = 0
                current += w
            
            return days_used <= days
        
        left = max(weights)       # minimum possible capacity
        right = sum(weights)      # maximum possible capacity
        
        while left < right:
            mid = (left + right) // 2
            
            if canShip(mid):
                right = mid      # try smaller capacity
            else:
                left = mid + 1   # need bigger capacity
        
        return left