class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(cur, open_count, close_count):
            # valid completed string
            if len(cur) == 2 * n:
                ans.append(cur)
                return

            # add '('
            if open_count < n:
                backtrack(cur + "(", open_count + 1, close_count)

            # add ')'
            if close_count < open_count:
                backtrack(cur + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return ans