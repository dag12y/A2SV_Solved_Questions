class Solution:
    import heapq

    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            y = -heapq.heappop(stones)  # largest
            x = -heapq.heappop(stones)  # second largest

            if y != x:
                heapq.heappush(stones, -(y - x))

        return -stones[0] if stones else 0