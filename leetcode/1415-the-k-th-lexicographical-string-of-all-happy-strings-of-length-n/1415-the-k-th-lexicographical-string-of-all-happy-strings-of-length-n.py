class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        letters = ['a', 'b', 'c']

        store = []
        def backtrack(path):
            if len(path)==n:
                store.append("".join(path))
                return
            
            for letter in letters:
                if path and path[-1] == letter:
                    continue
                path.append(letter)
                backtrack(path)
                path.pop()
            
        backtrack([])
        print(store)

        store.sort()
        # if k> len(store)
        if k>len(store):
            return ""
        
        return store[k-1]