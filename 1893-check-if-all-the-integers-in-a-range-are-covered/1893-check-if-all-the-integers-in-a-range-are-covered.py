class Solution(object):
    def isCovered(self, ranges, left, right):
        for x in range(left, right + 1):
            covered = False
            for l, r in ranges:
                if l <= x <= r:
                    covered = True
                    break
            if not covered:
                return False
        return True
