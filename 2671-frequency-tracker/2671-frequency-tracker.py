class FrequencyTracker:

    def __init__(self):
        self.count = {}  
        self.freq = {}  
    def add(self, number: int) -> None:
        prev = self.count.get(number, 0)
        nxt = prev + 1

        self.count[number] = nxt

        if prev > 0:
            self.freq[prev] -= 1

        self.freq[nxt] = self.freq.get(nxt, 0) + 1

    def deleteOne(self, number: int) -> None:
        if number not in self.count:
            return

        prev = self.count[number]
        nxt = prev - 1

        self.freq[prev] -= 1

        if nxt == 0:
            del self.count[number]
        else:
            self.count[number] = nxt
            self.freq[nxt] = self.freq.get(nxt, 0) + 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq.get(frequency, 0) > 0
