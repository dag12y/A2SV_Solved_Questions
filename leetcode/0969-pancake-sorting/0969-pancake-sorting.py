class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        n = len(arr)

        for curr_size in range(n, 1, -1):
            # Find index of the current largest number
            max_index = arr.index(curr_size)

            # If already in correct position, skip
            if max_index == curr_size - 1:
                continue

            # Step 1: Bring it to front (if not already at front)
            if max_index != 0:
                res.append(max_index + 1)
                arr[:max_index + 1] = reversed(arr[:max_index + 1])

            # Step 2: Move it to its correct position
            res.append(curr_size)
            arr[:curr_size] = reversed(arr[:curr_size])

        return res