class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """
        n = len(s)
        diff = [0] * (n + 1)

        for start, end, direction in shifts:
            val = 1 if direction == 1 else -1
            diff[start] += val
            diff[end + 1] -= val

        res = []
        curr = 0

        for i in range(n):
            curr += diff[i]

            shift = (ord(s[i]) - ord('a') + curr) % 26
            res.append(chr(shift + ord('a')))

        return "".join(res)
        