class Solution:
    import heapq
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []

        for i in range(len(heights) - 1):
            climb = heights[i + 1] - heights[i]

            if climb > 0:
                heapq.heappush(heap, climb)

            # More climbs than ladders
            if len(heap) > ladders:
                bricks -= heapq.heappop(heap)

            # Can't continue
            if bricks < 0:
                return i

        return len(heights) - 1