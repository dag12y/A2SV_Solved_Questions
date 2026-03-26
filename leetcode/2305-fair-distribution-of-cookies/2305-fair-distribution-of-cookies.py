class Solution:
    def distributeCookies(self, cookies: list[int], k: int) -> int:
        maxFair = float('inf')

        def backtrack(i, child):
            nonlocal maxFair

            # base case
            if i == len(cookies):
                maxFair = min(maxFair, max(child))
                return

            for j in range(k):

                # PRUNE 1: already worse than best
                if child[j] >= maxFair:
                    continue

                # PRUNE 2: avoid duplicate states
                if j > 0 and child[j] == child[j - 1]:
                    continue

                # pick
                child[j] += cookies[i]
                backtrack(i + 1, child)
                child[j] -= cookies[i]

                # PRUNE 3: stop if assigning to empty child
                if child[j] == 0:
                    break

        backtrack(0, [0]*k)
        return maxFair