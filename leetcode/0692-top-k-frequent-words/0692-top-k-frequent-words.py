class Solution:
    from collections import Counter
    import heapq
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)

        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap)

        ans = []

        for _ in range(k):
            freq, word = heapq.heappop(heap)
            ans.append(word)

        return ans
        