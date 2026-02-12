class RandomizedSet(object):

    def __init__(self):
        self.values=[]
        self.val_to_idx = {}

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.val_to_idx:
            return False

        self.values.append(val)
        self.val_to_idx[val] = len(self.values) - 1
        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.val_to_idx:
            return False

        idx = self.val_to_idx[val]
        last_val = self.values[-1]

        self.values[idx] = last_val
        self.val_to_idx[last_val] = idx

        self.values.pop()
        del self.val_to_idx[val]
        return True
        

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.values)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()