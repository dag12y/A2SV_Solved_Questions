class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        res = 0
        
        for house in houses:
            # find insertion position
            i = bisect.bisect_left(heaters, house)
            
            # distance to left heater
            left = float('inf') if i == 0 else house - heaters[i-1]
            
            # distance to right heater
            right = float('inf') if i == len(heaters) else heaters[i] - house
            
            # closest heater
            closest = min(left, right)
            
            res = max(res, closest)
        
        return res