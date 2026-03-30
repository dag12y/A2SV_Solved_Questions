class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        def solve(friends, index):
            if len(friends) == 1:
                return friends[0]
            
            index = (index + k - 1) % len(friends)
            friends.pop(index)
            
            return solve(friends, index)
        
        return solve(list(range(1, n+1)), 0)