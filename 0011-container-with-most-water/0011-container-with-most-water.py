class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start, end = 0, len(height) - 1
        max_area = 0

        while start < end:
            h = min(height[start], height[end])
            w = end - start
            area = h * w
            max_area = max(max_area, area)

            if height[start] < height[end]:
                start += 1
            else:
                end -= 1

        return max_area