class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict
        keys = list(set(map(lambda str : "".join(sorted(str)),strs)))
        temp=defaultdict(list)
        for str in strs:
            for key in keys:
                if key == ''.join(sorted(str)):
                    temp[key].append(str)
        ans= [val for val in temp.values()]
        return ans
        